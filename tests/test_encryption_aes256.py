import lxml.etree as ET
import pytest

from encryption_AES256 import PBEWithAES256, PREFIX_AES256


FREEPLANE_AES256_ENCRYPTED_CONTENT = (
    "FP-AES256-V1:"
    "V+dgFa6wTzthkTMlVBePW8hKuEVIXRNkdjy111e3C/szfVeEou6mmFRgqyV5dfNN6NN2qaX4ZMcQNWzfu1P+c0L02JgILJfnKvLZ321B8WKw+Dt5jPDrbMtlqDX6a0RPH38C7cR17VxQQ/aEhbLrKq21JJ5N4AInCgsJTInklLLZiS32Do6G4GB7Kx/Fm8q8RiurzkAPBX5F1WR5rBdpdAMGyVerMWKk2qRgoQPh/rBcSpEN4ayyA/rEx0dIjYLGkuHxsXc4OqcJMYF43N1DTvInErHbBVSTn7RFLdm2SFGLSc4CiHip98xOWl+5nGfVyQEKGy7aNZhiNR2MndfgtpXh56sK+OizNTu+afZhDHNNfJwu5RnDBYO8qGTWfDRwmIsm79OoynDiHpnjh2kbOvLXCFrMHxteeAXz1Xmw1fgkooUMMKlrXqjaBiqejgufctChi+TQ66GJHnMq+E7snuz/4bAiVCKDXf/7j2hx5/b9xWsNjJDEA3IZ1Ky+XTQ3LTrVwFTapxR+cRoALqMOvcNqYDkHmjpMx5V8gC2xrTsTFYYuZqCgWtH5GdJUUtOVIahuHNerci+t/9iLrogj6hELBjX5D7KLSeNY9q3G59KXYV827/CHq+trZMN31DuSJLqrwwWE4HVVknqy4OJTGYOZ2BeQakOf19IBTOGPJpjcss5UVRAZeKEKXo3y1X4q5xC0oL5jvU5ZhvafsNXLNlxZdT73P3fDzvDV6B3msm247nWBycJkuoU9eUaW1Bd59baX4N1qFY5zV7RO49fVmLcy07732Iigea0f16YhqmyAO1KpgDclfD7RpT7W1UCPwq9AkY7oFs9E+cTG7qgTueacOgodRVUfO6StLHrzvu6bAN26WWm2AggPOfA="
)


def test__encrypt_returns_freeplane_aes256_payload_and_roundtrips():
    cipher = PBEWithAES256()
    plain_text = '<node TEXT="roundtrip"><node TEXT="child"/></node>'

    encrypted_text = cipher.encrypt(plain_text, "test")
    decrypted_text = cipher.decrypt(encrypted_text, "test")

    assert encrypted_text.startswith(PREFIX_AES256)
    assert decrypted_text == plain_text


def test__encrypt_uses_fresh_salt_and_iv():
    cipher = PBEWithAES256()
    plain_text = "same plaintext"

    assert cipher.encrypt(plain_text, "test") != cipher.encrypt(plain_text, "test")


def test__decrypts_freeplane_aes256_content():
    decrypted = PBEWithAES256().decrypt(
        FREEPLANE_AES256_ENCRYPTED_CONTENT,
        "test",
    )

    node = ET.fromstring(decrypted.encode("utf-8"))

    assert node.tag == "node"
    assert node.get("TEXT") == "this is an attributed node with HTML content"
    assert node.find('./attribute[@NAME="type"]').get("VALUE") == "test"
    assert [child.get("TEXT") for child in node.findall("./node")] == [
        "erster Child",
        None,
        "dritter Child",
    ]


def test__decrypt_with_wrong_password_fails_authentication():
    with pytest.raises(ValueError):
        PBEWithAES256().decrypt(FREEPLANE_AES256_ENCRYPTED_CONTENT, "wrong")


def test__encrypt_subtree_returns_encrypted_xml_structure():
    cipher = PBEWithAES256()
    subtree = ET.fromstring(
        """
        <node TEXT="parent" ID="ID_1" CREATED="1" MODIFIED="2">
          <attribute NAME="type" VALUE="test"/>
          <node TEXT="child"/>
        </node>
        """
    )

    encrypted_node = cipher.encrypt_subtree(subtree, "test")
    decrypted_node = cipher.decrypt_subtree(encrypted_node, "test")

    assert encrypted_node.tag == "node"
    assert encrypted_node.get("TEXT") == "parent"
    assert encrypted_node.get("ENCRYPTED_CONTENT").startswith(PREFIX_AES256)
    assert encrypted_node.findall("./node") == []
    assert encrypted_node.findall("./attribute") == []

    assert ET.tostring(decrypted_node) == ET.tostring(subtree)
