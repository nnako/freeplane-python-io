from pathlib import Path

from freeplane import Mindmap


FIXTURE_PATH = Path(__file__).with_name("mm_encryption.mm")


def test__unlocked_encrypted_node_mutations_update_shadow_and_mark_dirty():
    """Verify writes on the virtual decrypted child update the shadow subtree."""
    mindmap = Mindmap(str(FIXTURE_PATH))
    node = mindmap.find_nodes(id="ID_1476345788")[0]

    assert node.unlock("test") is True
    inner = node.children[0]

    inner.plaintext = "changed title"
    inner.set_attribute("type", "changed")
    inner.notes = "private note"

    state = mindmap._encrypted_nodes[node._node]

    assert state.is_dirty is True
    assert state.decrypted_root.get("TEXT") == "changed title"
    assert state.decrypted_root.find('./attribute[@NAME="type"]').get("VALUE") == "changed"
    assert "private note" in inner.notes
    assert node.plaintext == "this is a parent node"


def test__regular_node_can_become_encrypted_wrapper_in_memory():
    """Verify set_encryption_password() prepares encrypted persistence."""
    mindmap = Mindmap()
    child = mindmap.rootnode.add_child("secret")
    child.add_attribute("kind", "x")
    child.notes = "hidden note"

    assert child.set_encryption_password("test") is True

    state = mindmap._encrypted_nodes[child._node]
    inner = child.children[0]

    assert child.is_encrypted is True
    assert child.is_unlocked is True
    assert child._node.get("ENCRYPTED_CONTENT")
    assert child._node.findall("./attribute") == []
    assert child._node.findall("./node") == []
    assert child.plaintext == "secret"
    assert child.attributes == {}
    assert inner.attributes == {"kind": "x"}
    assert inner.notes == "hidden note"
    assert state.password == "test"
    assert state.is_dirty is False


def test__refreshing_an_unlocked_encrypted_node_marks_it_for_reencryption():
    """Verify password changes on unlocked encrypted nodes mark them dirty."""
    mindmap = Mindmap(str(FIXTURE_PATH))
    node = mindmap.find_nodes(id="ID_1476345788")[0]

    node.unlock("test")
    state = mindmap._encrypted_nodes[node._node]
    state.is_dirty = False

    assert node.set_encryption_password("override") is True

    assert state.password == "override"
    assert state.is_dirty is True
