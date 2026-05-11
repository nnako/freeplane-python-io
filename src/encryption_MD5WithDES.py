"""

    pbe_with_md5_and_triple_des
    ~~~~~~~~~~~~
    This module provides ciphers that implement 'PBE With MD5 And Triple DES' and 'PBE With MD5 And DES' algorithms

    :copyright: (c) 2017 by Anton Koba (anton.koba@gmail.com)
    :license: MIT

"""

import base64
import copy
import hashlib
import os
from abc import ABC, abstractmethod
from typing import Any, Union

from Crypto.Cipher import DES, DES3

try:
    import lxml.etree as ET
except ImportError:  # pragma: no cover - optional dependency during packaging
    ET = None


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

    def encrypt(self, plain_text: str, password: str) -> str:
        """
        Encrypt plain text with the given password.

        The return value matches Freeplane's legacy attribute format:

            "<salt_base64> <ciphertext_base64>"

        Args:
            plain_text: Plain text to encrypt.
            password: Password used for encryption.

        Returns:
            Freeplane-compatible encrypted payload.
        """
        padded_text = self._pad_plain_text(plain_text.encode("utf-8"))
        salt = os.urandom(8)
        dk, iv = self._get_derived_key_and_iv(password.encode("utf-8"), salt)
        des = self._build_cipher(dk, iv)
        encrypted_text = des.encrypt(padded_text)
        return self._encode_payload(salt, encrypted_text)

    def decrypt(self, encoded_text: str, password: str) -> str:
        """
        Decrypt an encrypted Freeplane payload with the given password.

        Args:
            encoded_text: Freeplane-style encrypted payload.
            password: Password used for decryption.

        Returns:
            Decrypted plain text.
        """
        salt, encrypted_text_message = self._decode_payload(encoded_text)
        dk, iv = self._get_derived_key_and_iv(password.encode("utf-8"), salt)
        des = self._build_cipher(dk, iv)
        decrypted_bytes = des.decrypt(encrypted_text_message)
        return self._unpad_decrypted_message(decrypted_bytes).decode("utf-8")

    def encrypt_subtree(
        self,
        subtree: Union[str, Any],
        password: str,
        *,
        keep_outer_attributes: bool = True,
    ) -> Any:
        """Encrypt a Freeplane subtree into an XML node with ENCRYPTED_CONTENT.

        Args:
            subtree: lxml node or XML string representing the subtree root.
            password: Password used for encryption.
            keep_outer_attributes: Whether to keep the original node attributes
                on the encrypted wrapper node.

        Returns:
            Encrypted lxml node structure.
        """
        source_node = self._coerce_xml_node(subtree)
        encrypted_payload = self.encrypt(
            self._serialize_xml_node(source_node),
            password,
        )

        encrypted_node = ET.Element(source_node.tag)
        if keep_outer_attributes:
            for key, value in source_node.attrib.items():
                encrypted_node.attrib[key] = value

        encrypted_node.attrib["ENCRYPTED_CONTENT"] = encrypted_payload
        return encrypted_node

    def decrypt_subtree(
        self,
        encrypted_subtree: Union[str, Any],
        password: str,
    ) -> Any:
        """Decrypt a Freeplane encrypted XML node into its original subtree.

        Args:
            encrypted_subtree: lxml node or XML string containing an
                ENCRYPTED_CONTENT attribute.
            password: Password used for decryption.

        Returns:
            Decrypted lxml subtree root.
        """
        encrypted_node = self._coerce_xml_node(encrypted_subtree)
        encrypted_payload = encrypted_node.get("ENCRYPTED_CONTENT", "")
        if not encrypted_payload:
            raise ValueError("encrypted_subtree must contain ENCRYPTED_CONTENT")
        decrypted_text = self.decrypt(encrypted_payload, password)
        return self._coerce_xml_node(decrypted_text)

    def _encode_payload(self, salt: bytes, encrypted_text: bytes) -> str:
        """Build the Freeplane-compatible encrypted payload string."""
        salt_base64 = base64.b64encode(salt).decode("ascii")
        encrypted_base64 = base64.b64encode(encrypted_text).decode("ascii")
        return f"{salt_base64} {encrypted_base64}"

    def _decode_payload(self, encoded_text: str) -> tuple[bytes, bytes]:
        """
        Freeplane stores encrypted nodes in XML as:

        within freeplane, the crypted nodes are written in a specific
        format within the XML file:

          <node
            TEXT="<node-text>"
            ENCRYPTED_CONTENT="<salt_base64> <content_base64>"
            POSITION=...
            ID=...
            CREATED=...
            MODIFIED=...
          />

        Older helper code may also pass a single base64 string containing
        salt + ciphertext. Support both forms.
        """

        if " " in encoded_text:
            salt_base64, content_base64 = encoded_text.split(" ", 1)
            return base64.b64decode(salt_base64), base64.b64decode(content_base64.strip())

        decoded = base64.b64decode(encoded_text)
        return decoded[:8], decoded[8:]

    def _coerce_xml_node(self, subtree: Union[str, Any]) -> Any:
        """Convert a subtree input to an lxml node."""
        if ET is None:
            raise ImportError("lxml is required for subtree encryption helpers")

        if hasattr(subtree, "tag") and hasattr(subtree, "attrib"):
            return copy.deepcopy(subtree)

        if isinstance(subtree, str):
            return ET.fromstring(subtree.encode("utf-8"))

        raise TypeError("subtree must be an XML string or lxml element")

    def _serialize_xml_node(self, subtree: Any) -> str:
        """Serialize an lxml subtree without XML declaration."""
        if ET is None:
            raise ImportError("lxml is required for subtree encryption helpers")

        return ET.tostring(
            subtree,
            pretty_print=True,
            method="xml",
            encoding="utf-8",
        ).decode("utf-8")

    def _build_cipher(self, dk, iv):
        des_class = self._get_des_encoder_class()
        if self.triple_des:
            dk = DES3.adjust_key_parity(dk)
        return des_class.new(dk, des_class.MODE_CBC, iv)


    def _pad_plain_text(self, plain_text: bytes) -> bytes:
        """
        Pad plain text up to the whole block size using PKCS5/PKCS7 bytes.

        Args:
            plain_text: Plain text bytes to pad.

        Returns:
            Padded bytes.
        """
        pad_number = BLOCK_LENGTH_BYTES - (len(plain_text) % BLOCK_LENGTH_BYTES)
        return plain_text + bytes([pad_number]) * pad_number


    def _unpad_decrypted_message(self, decrypted_message: bytes) -> bytes:
        """Remove PKCS5/PKCS7 padding from a decrypted message.

        Args:
            decrypted_message: Decrypted bytes.

        Returns:
            Unpadded bytes.
        """
        pad_value = decrypted_message[-1]
        if pad_value == 0 or pad_value > BLOCK_LENGTH_BYTES:
            return decrypted_message
        if decrypted_message[-pad_value:] != bytes([pad_value]) * pad_value:
            return decrypted_message
        return decrypted_message[:-pad_value]


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
