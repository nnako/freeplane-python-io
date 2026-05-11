import lxml.etree as ET

from encryption_AES256 import PREFIX_AES256
from freeplane import Mindmap


FREEPLANE_AES256_ENCRYPTED_CONTENT = (
    "FP-AES256-V1:"
    "V+dgFa6wTzthkTMlVBePW8hKuEVIXRNkdjy111e3C/szfVeEou6mmFRgqyV5dfNN6NN2qaX4ZMcQNWzfu1P+c0L02JgILJfnKvLZ321B8WKw+Dt5jPDrbMtlqDX6a0RPH38C7cR17VxQQ/aEhbLrKq21JJ5N4AInCgsJTInklLLZiS32Do6G4GB7Kx/Fm8q8RiurzkAPBX5F1WR5rBdpdAMGyVerMWKk2qRgoQPh/rBcSpEN4ayyA/rEx0dIjYLGkuHxsXc4OqcJMYF43N1DTvInErHbBVSTn7RFLdm2SFGLSc4CiHip98xOWl+5nGfVyQEKGy7aNZhiNR2MndfgtpXh56sK+OizNTu+afZhDHNNfJwu5RnDBYO8qGTWfDRwmIsm79OoynDiHpnjh2kbOvLXCFrMHxteeAXz1Xmw1fgkooUMMKlrXqjaBiqejgufctChi+TQ66GJHnMq+E7snuz/4bAiVCKDXf/7j2hx5/b9xWsNjJDEA3IZ1Ky+XTQ3LTrVwFTapxR+cRoALqMOvcNqYDkHmjpMx5V8gC2xrTsTFYYuZqCgWtH5GdJUUtOVIahuHNerci+t/9iLrogj6hELBjX5D7KLSeNY9q3G59KXYV827/CHq+trZMN31DuSJLqrwwWE4HVVknqy4OJTGYOZ2BeQakOf19IBTOGPJpjcss5UVRAZeKEKXo3y1X4q5xC0oL5jvU5ZhvafsNXLNlxZdT73P3fDzvDV6B3msm247nWBycJkuoU9eUaW1Bd59baX4N1qFY5zV7RO49fVmLcy07732Iigea0f16YhqmyAO1KpgDclfD7RpT7W1UCPwq9AkY7oFs9E+cTG7qgTueacOgodRVUfO6StLHrzvu6bAN26WWm2AggPOfA="
)


def _write_aes256_map(path):
    """
    Write a minimal Freeplane map containing one AES-256 encrypted wrapper.

    Args:
        path: Destination path for the temporary mindmap file.
    """
    root = ET.Element("map", version="freeplane 1.12.1")
    root_node = ET.SubElement(root, "node", TEXT="root", ID="ID_ROOT")
    ET.SubElement(
        root_node,
        "node",
        TEXT='this is an AES256-encrypted node with PW "test1"',
        ENCRYPTED_CONTENT=FREEPLANE_AES256_ENCRYPTED_CONTENT,
        POSITION="bottom_or_right",
        ID="ID_AES_WRAPPER",
        CREATED="1761499227779",
        MODIFIED="1778509225166",
    )
    ET.ElementTree(root).write(str(path), encoding="utf-8", xml_declaration=False)


def test__mindmap_registers_des_and_aes256_ciphers():
    """Verify the map can try legacy DES first and AES-256 second."""
    mindmap = Mindmap()

    assert [cipher.__class__.__name__ for cipher in mindmap._ciphers] == [
        "PBEWithMD5AndDES",
        "PBEWithAES256",
    ]
    assert mindmap._cipher.__class__.__name__ == "PBEWithMD5AndDES"


def test__node_decrypt_falls_back_to_aes256_after_des_fails(tmp_path):
    """Verify an AES-256 node unlocks through the public Node.decrypt() API."""
    map_path = tmp_path / "aes256.mm"
    _write_aes256_map(map_path)
    mindmap = Mindmap(str(map_path))
    wrapper = mindmap.find_nodes(id="ID_AES_WRAPPER")[0]

    assert wrapper.is_encrypted is True
    assert wrapper.is_unlocked is False
    assert wrapper.decrypt("test") is True

    state = mindmap._encrypted_nodes[wrapper._node]
    assert state.cipher.__class__.__name__ == "PBEWithAES256"
    assert wrapper.is_unlocked is True
    assert wrapper.children[0].plaintext == "this is an attributed node with HTML content"
    assert wrapper.children[0].attributes == {"type": "test"}


def test__save_preserves_aes256_cipher_for_modified_aes256_node(tmp_path):
    """Verify modified AES-256 wrappers are re-encrypted with AES-256."""
    map_path = tmp_path / "aes256.mm"
    output_path = tmp_path / "aes256_saved.mm"
    _write_aes256_map(map_path)
    mindmap = Mindmap(str(map_path), encryption_passwords=["wrong", "test"])
    wrapper = mindmap.find_nodes(id="ID_AES_WRAPPER")[0]

    wrapper.children[0].plaintext = "changed AES title"
    mindmap.save(str(output_path))

    raw_root = ET.parse(str(output_path)).getroot()
    raw_wrapper = raw_root.find(".//node[@ID='ID_AES_WRAPPER']")
    assert raw_wrapper.get("ENCRYPTED_CONTENT").startswith(PREFIX_AES256)

    reloaded = Mindmap(str(output_path))
    reloaded_wrapper = reloaded.find_nodes(id="ID_AES_WRAPPER")[0]
    assert reloaded_wrapper.decrypt("test") is True
    assert reloaded_wrapper.children[0].plaintext == "changed AES title"
