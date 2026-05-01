from pathlib import Path

import lxml.etree as ET

from freeplane import Mindmap


FIXTURE_PATH = Path(__file__).with_name("mm_encryption.mm")


def test__save_reencrypts_modified_loaded_wrapper_nodes(tmp_path):
    """Verify modified unlocked wrapper nodes are re-encrypted on save."""
    mindmap = Mindmap(str(FIXTURE_PATH))
    node = mindmap.find_nodes(id="ID_1476345788")[0]

    node.unlock("test")
    inner = node.children[0]
    inner.plaintext = "changed title"
    inner.set_attribute("type", "changed")

    output_path = tmp_path / "encrypted_saved.mm"
    mindmap.save(str(output_path))

    raw_root = ET.parse(str(output_path)).getroot()
    raw_wrapper = raw_root.find(".//node[@ID='ID_1476345788']")
    assert raw_wrapper is not None
    assert raw_wrapper.get("ENCRYPTED_CONTENT")
    assert raw_wrapper.findall("./node") == []
    assert raw_wrapper.findall("./attribute") == []

    reloaded = Mindmap(str(output_path))
    reloaded_node = reloaded.find_nodes(id="ID_1476345788")[0]
    assert reloaded_node.unlock("test") is True
    assert reloaded_node.plaintext == "this is a parent node"
    assert reloaded_node.children[0].plaintext == "changed title"
    assert reloaded_node.children[0].attributes["type"] == "changed"


def test__save_persists_newly_encrypted_in_memory_wrapper_nodes(tmp_path):
    """Verify nodes encrypted in memory are written back as encrypted wrappers."""
    mindmap = Mindmap()
    child = mindmap.rootnode.add_child("secret")
    child.add_attribute("kind", "x")
    child.encrypt("test")
    child.children[0].plaintext = "secret changed"

    output_path = tmp_path / "newly_encrypted.mm"
    mindmap.save(str(output_path))

    raw_root = ET.parse(str(output_path)).getroot()
    raw_wrapper = raw_root.find(f".//node[@ID='{child.id}']")
    assert raw_wrapper is not None
    assert raw_wrapper.get("ENCRYPTED_CONTENT")
    assert raw_wrapper.findall("./attribute") == []
    assert raw_wrapper.findall("./node") == []

    reloaded = Mindmap(str(output_path))
    reloaded_node = reloaded.find_nodes(id=child.id)[0]
    assert reloaded_node.unlock("test") is True
    assert reloaded_node.plaintext == "secret"
    assert reloaded_node.children[0].plaintext == "secret changed"
    assert reloaded_node.children[0].attributes == {"kind": "x"}
