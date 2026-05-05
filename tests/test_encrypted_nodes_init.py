from pathlib import Path

from freeplane import Mindmap


FIXTURE_PATH = Path(__file__).with_name("mm_encryption.mm")


def test__mindmap_init_unlocks_encrypted_nodes_with_constructor_passwords():
    """Verify encrypted nodes can be unlocked while creating the map object."""
    mindmap = Mindmap(str(FIXTURE_PATH), encryption_passwords=["wrong", "test"])

    wrapper = mindmap.find_nodes(id="ID_1476345788")[0]

    assert mindmap.passwords == ["wrong", "test"]
    assert wrapper.is_encrypted is True
    assert wrapper.is_unlocked is True
    assert wrapper.has_children is True
    assert wrapper.children[0].plaintext == "this is an attributed node with HTML content"


def test__mindmap_init_keeps_encrypted_nodes_locked_if_no_password_matches():
    """Verify constructor passwords do not unlock with only wrong candidates."""
    mindmap = Mindmap(str(FIXTURE_PATH), encryption_passwords=["wrong"])

    wrapper = mindmap.find_nodes(id="ID_1476345788")[0]

    assert mindmap.passwords == ["wrong"]
    assert wrapper.is_encrypted is True
    assert wrapper.is_unlocked is False
    assert wrapper.has_children is False
