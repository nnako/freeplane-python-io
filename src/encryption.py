"""

    pbe_with_md5_and_triple_des
    ~~~~~~~~~~~~
    This module provides ciphers that implement 'PBE With MD5 And Triple DES' and 'PBE With MD5 And DES' algorithms

    :copyright: (c) 2017 by Anton Koba (anton.koba@gmail.com)
    :license: MIT

"""

from abc import ABC, abstractmethod
import binascii
import base64
import hashlib
import os
from Crypto.Cipher import DES, DES3


BLOCK_LENGTH_BYTES = 8  # pad incoming message to whole length of block

# DERIVED_KEY_ITERATIONS = 1000  # cycles to hash over to produce dk and iv
DERIVED_KEY_ITERATIONS = 19  # cycles to hash over to produce dk and iv


class AbstractPBEWithMD5AndDES(ABC):
    """ Defines basic algorithm for PBE With MD5 And DES / Triple DES (DESede)
    DES and Triple DES versions differ in the way how the derived key (dk) and
    initialization vector (iv) are generated
    """

    # use DES3 (triple DES a.k.a. DESede) or plain DES
    triple_des = True

    def __init__(self, iterations=DERIVED_KEY_ITERATIONS):
        super().__init__()
        self.iterations = iterations

    def encrypt(self, plain_text, password):
        """
        Encrypts plain text with given password

        :param plain_text: plain text to decrypt
        :param password: password to decrypt with
        :return: base64-encoded encrypted text
        """

        # pad message up to a whole block size
        padded_text = self._pad_plain_text(plain_text)

        # generate Salt as 8 random bytes
        salt = os.urandom(8)

        # get dk and iv using proper algorithm (either for DES ot DES3), password as bytes
        (dk, iv) = self._get_derived_key_and_iv(password.encode('utf-8'), salt)

        # get proper class (DES/DES3) to instantiate and use for encoding
        des = self._build_cipher(dk, iv)

        # do the encryption (use bytes not string)
        #encrypted_text = des.encrypt(padded_text)
        encrypted_text = des.encrypt(padded_text.encode('utf-8'))

        # return encrypted text prepended with salt, all base64-encoded
        return base64.b64encode(salt + encrypted_text)

    def decrypt(self, encoded_text, password):
        """
        Decrypts encoded_text with given password

        :param encoded_text: encoded string
        :param password: password to decrypt with
        :return: decrypted plain text as string (bytes)
        """
        salt, encrypted_text_message = self._decode_payload(encoded_text)


        # get dk and iv using proper algorithm (either for DES or DES3)
        (dk, iv) = self._get_derived_key_and_iv(password.encode('utf-8'), salt)

        # get proper class (DES/DES3) to instantiate and use for decoding
        des = self._build_cipher(dk, iv)

        # freeplane stores XML fragments, so remove PKCS5 padding on bytes first
        decrypted_bytes = des.decrypt(encrypted_text_message)
        return self._unpad_decrypted_message(decrypted_bytes).decode("utf-8")


    def _decode_payload(self, encoded_text):
        """
        Freeplane stores encrypted nodes in XML as:

            ENCRYPTED_CONTENT="<salt_base64> <content_base64>"

        Older helper code may also pass a single base64 string containing
        salt + ciphertext. Support both forms.
        """

        if " " in encoded_text:
            salt_base64, content_base64 = encoded_text.split(" ", 1)
            return base64.b64decode(salt_base64), base64.b64decode(content_base64.strip())

        decoded = base64.b64decode(encoded_text)
        return decoded[:8], decoded[8:]


    def _build_cipher(self, dk, iv):
        des_class = self._get_des_encoder_class()
        if self.triple_des:
            dk = DES3.adjust_key_parity(dk)
        return des_class.new(dk, des_class.MODE_CBC, iv)


    def _pad_plain_text(self, plain_text):
        """
        Pads plain text up to the whole length of block (8 bytes).
        We are adding chars which are equal to the number of padded bytes.
        i.e. 'hello' -> 'hello/x03/x03/x03'
        :param plain_text: plain text to be padded (bytes)
        :return: padded bytes
        """
        pad_number = BLOCK_LENGTH_BYTES - (len(plain_text) % BLOCK_LENGTH_BYTES)
        result = plain_text
        for i in range(pad_number):
            result += chr(pad_number)
        return result


    def _unpad_decrypted_message(self, decrypted_message):
        """ Decrypted message could be padded on the end, last character means number of
        :param decrypted_message: with PKCS7 padding
        :return: unpadded text
        """

        if isinstance(decrypted_message, bytes):
            pad_value = decrypted_message[-1]
            if pad_value == 0 or pad_value > BLOCK_LENGTH_BYTES:
                return decrypted_message
            if decrypted_message[-pad_value:] != bytes([pad_value]) * pad_value:
                return decrypted_message
            return decrypted_message[:-pad_value]

        message_length = len(decrypted_message)
        pad_str = decrypted_message[-1]

        # try to identify a pad value from the incoming string
        try:
            pad_value = int(binascii.b2a_hex(pad_str.encode("utf8")))
        except:
            # no padding elements identified
            return decrypted_message

        if pad_value > 8:
            # no padding used
            return decrypted_message

        else:
            # where real data ends
            position = message_length - pad_value

            return decrypted_message[:position]


    def _get_des_encoder_class(self):
        return DES3 if self.triple_des else DES


    @abstractmethod
    def _get_derived_key_and_iv(self, password, salt):
        return None


class PBEWithMD5AndDES(AbstractPBEWithMD5AndDES):

    triple_des = False

    def _get_derived_key_and_iv(self, password, salt):
        """
        Returns tuple of dk(8 bytes) and iv(8 bytes) for DES

        Logic: concatenate password + salt and hash them given number of iterations
        (result of hash function is given to it an an input on following iteration)

        :param password: password used for encryption/decryption
        :param salt: salt
        :param cycles: number of hashing iterations
        :return: (8 bytes dk, 8 bytes iv)
        """
        key = password + salt
        for i in range(self.iterations):
            m = hashlib.md5(key)
            key = m.digest()
        return key[:8], key[8:]


class PBEWithMD5AndTripleDES(AbstractPBEWithMD5AndDES):

    def _get_derived_key_and_iv(self, password, salt):
        """
        Returns tuple of dk(24 bytes) and iv(8 bytes) for DES3 (Triple DES, DESede)

        Logic:
        Salt will be split in two halves and processed separately.
        1. If 2 halves of salt are same, reverse first part
        2. For each half of salt:
            - Start hashing loop with half of salt + password (not password + salt as in DES keys)
            concatenate output of hash with password on each iteration
            - iterate for each half of salt given number of times
        3. Join two parts of hashes (16 + 16 bytes)
        4. First 24 bytes will be used as key for DES3, latest 8 bytes - iv for DES3

        :param password: password used for encryption/decryption
        :param salt: salt
        :param cycles: number of hashing iterations (see description)
        :return: (24 bytes dk, 8 bytes iv)
        """

        # reverse first half of salt if two halves are the same
        if salt[:4] == salt[4:]:
            salt = salt[-5::-1] + salt[4:]

        # do part 1
        part1_to_hash = salt[:4]
        for i in range(self.iterations):
            m = hashlib.md5(part1_to_hash + password)
            part1_to_hash = m.digest()

        # do part 2
        part2_to_hash = salt[4:]
        for i in range(self.iterations):
            m = hashlib.md5(part2_to_hash + password)
            part2_to_hash = m.digest()

        result = part1_to_hash + part2_to_hash

        # key, iv
        return result[:24], result[24:]
