"""
Freeplane AES-256 encrypted node support.

Freeplane stores AES-256 encrypted node content as:

    FP-AES256-V1:<base64(salt || iv || ciphertext || tag)>

The key is derived from the password with PBKDF2-HMAC-SHA256. Encryption uses
AES-256-GCM with a 128-bit authentication tag.
"""

import base64
import copy
import os
from typing import Any, Union

from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Protocol.KDF import PBKDF2

try:
    import lxml.etree as ET
except ImportError:  # pragma: no cover - optional dependency during packaging
    ET = None


PREFIX_AES256 = "FP-AES256-V1:"
SALT_LENGTH_BYTES = 16
IV_LENGTH_BYTES = 12
TAG_LENGTH_BYTES = 16
KEY_LENGTH_BYTES = 32
DERIVED_KEY_ITERATIONS = 100000


class PBEWithAES256:
    """Freeplane-compatible AES-256-GCM encryption helper."""

    def __init__(self, iterations: int = DERIVED_KEY_ITERATIONS):
        self.iterations = iterations

    def encrypt(self, plain_text: str, password: str) -> str:
        """
        Encrypt plain text with the given password.

        Returns:
            Freeplane AES-256 payload in the ``FP-AES256-V1:...`` format.
        """
        salt = os.urandom(SALT_LENGTH_BYTES)
        iv = os.urandom(IV_LENGTH_BYTES)
        key = self._derive_key(password, salt)
        cipher = AES.new(key, AES.MODE_GCM, nonce=iv, mac_len=TAG_LENGTH_BYTES)
        encrypted_text, tag = cipher.encrypt_and_digest(plain_text.encode("utf-8"))
        return self._encode_payload(salt, iv, encrypted_text + tag)

    def decrypt(self, encoded_text: str, password: str) -> str:
        """
        Decrypt a Freeplane AES-256 payload with the given password.

        Args:
            encoded_text: Payload in the ``FP-AES256-V1:...`` format.
            password: Password used for decryption.

        Returns:
            Decrypted plain text.
        """
        salt, iv, encrypted_text, tag = self._decode_payload(encoded_text)
        key = self._derive_key(password, salt)
        cipher = AES.new(key, AES.MODE_GCM, nonce=iv, mac_len=TAG_LENGTH_BYTES)
        return cipher.decrypt_and_verify(encrypted_text, tag).decode("utf-8")

    def encrypt_subtree(
        self,
        subtree: Union[str, Any],
        password: str,
        *,
        keep_outer_attributes: bool = True,
    ) -> Any:
        """Encrypt a Freeplane subtree into an XML node with ENCRYPTED_CONTENT."""
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
        """Decrypt a Freeplane encrypted XML node into its original subtree."""
        encrypted_node = self._coerce_xml_node(encrypted_subtree)
        encrypted_payload = encrypted_node.get("ENCRYPTED_CONTENT", "")
        if not encrypted_payload:
            raise ValueError("encrypted_subtree must contain ENCRYPTED_CONTENT")
        decrypted_text = self.decrypt(encrypted_payload, password)
        return self._coerce_xml_node(decrypted_text)

    def _derive_key(self, password: str, salt: bytes) -> bytes:
        return PBKDF2(
            password.encode("utf-8"),
            salt,
            dkLen=KEY_LENGTH_BYTES,
            count=self.iterations,
            hmac_hash_module=SHA256,
        )

    def _encode_payload(self, salt: bytes, iv: bytes, encrypted_text: bytes) -> str:
        payload = salt + iv + encrypted_text
        return PREFIX_AES256 + base64.b64encode(payload).decode("ascii")

    def _decode_payload(self, encoded_text: str) -> tuple[bytes, bytes, bytes, bytes]:
        if not encoded_text.startswith(PREFIX_AES256):
            raise ValueError("encoded_text must start with FP-AES256-V1:")

        payload = base64.b64decode(encoded_text[len(PREFIX_AES256) :])
        minimum_length = SALT_LENGTH_BYTES + IV_LENGTH_BYTES + TAG_LENGTH_BYTES
        if len(payload) < minimum_length:
            raise ValueError("encoded_text is too short")

        salt_end = SALT_LENGTH_BYTES
        iv_end = salt_end + IV_LENGTH_BYTES
        tag_start = len(payload) - TAG_LENGTH_BYTES
        return (
            payload[:salt_end],
            payload[salt_end:iv_end],
            payload[iv_end:tag_start],
            payload[tag_start:],
        )

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


AES256Encrypter = PBEWithAES256
