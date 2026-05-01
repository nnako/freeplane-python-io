from pathlib import Path

from freeplane import Mindmap


FIXTURE_PATH = Path(__file__).with_name("mm_encryption.mm")


def test__encrypted_node_read_accessors_use_decrypted_shadow_subtree():
    """Verify unlocked encrypted nodes keep wrapper identity and expose a shadow child."""
    mindmap = Mindmap(str(FIXTURE_PATH))
    node = mindmap.find_nodes(id="ID_1476345788")[0]

    assert node.is_encrypted is True
    assert node.is_unlocked is False
    assert node.plaintext == "this is a parent node"
    assert node.has_children is False

    assert node.unlock("test") is True

    assert node.is_unlocked is True
    assert node.plaintext == "this is a parent node"
    assert node.attributes == {}
    assert node.has_children is True
    assert [child.plaintext for child in node.children] == [
        "this is an attributed node with HTML content",
    ]
    assert node.children[0].attributes == {"type": "test"}
    assert [child.plaintext for child in node.children[0].children] == [
        "erster Child",
        "zweiter Child",
        "dritter Child",
    ]


def test__encrypted_node_can_drop_decrypted_shadow_state_again():
    """Verify lock() restores wrapper-based read behavior."""
    mindmap = Mindmap(str(FIXTURE_PATH))
    node = mindmap.find_nodes(id="ID_1476345788")[0]

    node.unlock("test")
    node.lock()

    assert node.is_unlocked is False
    assert node.plaintext == "this is a parent node"
    assert node.has_children is False
