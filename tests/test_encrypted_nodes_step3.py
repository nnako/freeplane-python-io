from pathlib import Path

from freeplane import Mindmap


FIXTURE_PATH = Path(__file__).with_name("mm_encryption.mm")


def test__mindmap_registers_encrypted_wrapper_nodes_from_loaded_file():
    """Verify encrypted wrapper nodes are indexed during map load."""
    mindmap = Mindmap(str(FIXTURE_PATH))

    assert len(mindmap._encrypted_nodes) == 2

    wrapper = mindmap.find_nodes(id="ID_1476345788")[0]
    state = mindmap._encrypted_nodes[wrapper._node]
    assert state.wrapper_node.get("ENCRYPTED_CONTENT")
    assert state.original_payload == state.wrapper_node.get("ENCRYPTED_CONTENT")
    assert state.decrypted_root is None
    assert state.is_unlocked is False


def test__mindmap_unlocks_registered_nodes_with_matching_password():
    """Verify ordered password trials can unlock a registered wrapper node."""
    mindmap = Mindmap(str(FIXTURE_PATH))

    unlocked_count = mindmap.unlock_encrypted_nodes(["wrong", "test"])

    assert unlocked_count == 1
    wrapper = mindmap.find_nodes(id="ID_1476345788")[0]
    state = mindmap._encrypted_nodes[wrapper._node]
    assert state.is_unlocked is True
    assert state.password == "test"
    assert state.decrypted_root.tag == "node"
    assert state.decrypted_root.get("TEXT") == "this is an attributed node with HTML content"


def test__mindmap_can_unlock_registered_nodes_via_map_passwords():
    """Verify stored map passwords are used when no explicit list is given."""
    mindmap = Mindmap(str(FIXTURE_PATH))
    mindmap.set_passwords(["wrong", "test"])

    unlocked_count = mindmap.unlock_encrypted_nodes()

    assert unlocked_count == 1
    wrapper = mindmap.find_nodes(id="ID_1476345788")[0]
    state = mindmap._encrypted_nodes[wrapper._node]
    assert state.is_unlocked is True
