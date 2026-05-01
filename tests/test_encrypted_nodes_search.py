from pathlib import Path

from freeplane import Mindmap


FIXTURE_PATH = Path(__file__).with_name("mm_encryption.mm")


def test__mindmap_find_nodes_sees_virtual_decrypted_subtree_nodes():
    """Verify map-level search sees unlocked encrypted subtree content."""
    mindmap = Mindmap(str(FIXTURE_PATH))
    wrapper = mindmap.find_nodes(id="ID_1476345788")[0]
    assert wrapper.unlock("test") is True

    matches = mindmap.find_nodes(id="ID_974360361")

    assert len(matches) == 1
    assert matches[0].plaintext == "erster Child"
    assert matches[0].parent.plaintext == "this is an attributed node with HTML content"


def test__node_find_nodes_sees_virtual_decrypted_descendants():
    """Verify subtree search walks unlocked encrypted descendants."""
    mindmap = Mindmap(str(FIXTURE_PATH))
    wrapper = mindmap.find_nodes(id="ID_1476345788")[0]
    assert wrapper.unlock("test") is True

    matches = wrapper.find_nodes(id="ID_1970961842")

    assert len(matches) == 1
    assert matches[0].plaintext == "dritter Child"
    assert matches[0].parent.plaintext == "this is an attributed node with HTML content"


def test__node_find_children_sees_virtual_decrypted_root_child():
    """Verify direct-child search returns the virtual decrypted subtree root."""
    mindmap = Mindmap(str(FIXTURE_PATH))
    wrapper = mindmap.find_nodes(id="ID_1476345788")[0]
    assert wrapper.unlock("test") is True

    matches = wrapper.find_children(core="this is an attributed node with HTML content")

    assert len(matches) == 1
    assert matches[0].plaintext == "this is an attributed node with HTML content"
    assert matches[0].parent.id == "ID_1476345788"
