import io
import os
import types
import tempfile
import lxml.etree as ET
import pytest

import freeplane
from freeplane import Mindmap, Node

@pytest.fixture(autouse=True)
def reset_class_counters():
    """Sorgt für sauberen Zustand zwischen Tests."""
    Mindmap._num_of_maps = 0
    Mindmap._global_node_id_incr = 0
    Mindmap._global_node_id_seed = "250101"  # fixiertes Datum für reproduzierbare IDs

def test__init__creates_basic_structure():
    mm = Mindmap()
    assert isinstance(mm._mindmap, ET.Element)
    assert mm._mindmap.tag == "map"
    assert "version" in mm._mindmap.attrib
    assert mm._rootnode.tag == "node"
    assert Mindmap.get_num_of_maps() == 1


def test__create_node_id__increments_properly():
    mm = Mindmap()
    id1 = Mindmap.create_node_id(mm)
    id2 = Mindmap.create_node_id(mm)
    assert id1 != id2
    assert id1.startswith("ID_250101")
    assert id2.endswith("0003")         # "3" after two node creations as the "rootnode" has been created first


# def test_create_node_creates_valid_node(monkeypatch):
#     # Mock Hilfsfunktionen, um externe Abhängigkeiten zu vermeiden
#     monkeypatch.setattr("freeplane.update_date_attribute_in_node", lambda **kw: None)
#     monkeypatch.setattr("freeplane.Branch", lambda: types.SimpleNamespace())
#
#     mm = Mindmap()
#     fpNode = mm.create_node(core="Hello")
#     assert isinstance(fpNode, Node)
#     assert hasattr(fpNode, "plaintext")
#     assert fpNode.plaintext == "Hello"


def test__rootnode__returns_node_instance():
    mm = Mindmap()
    rn = mm.rootnode
    assert isinstance(rn, Node)
    assert rn._node.tag == "node"
    # assert rn.mindmap is mm


def test__styles__returns_dict_with_expected_keys():
    mm = Mindmap()
    styles = mm.styles
    # Styles dict enthält vordefinierte "styles.user-defined"-Einträge
    assert isinstance(styles, dict)
    for v in styles.values():
        assert isinstance(v, dict)
        assert "color" in v or "fontname" in v or "fontsize" in v


def test__add_style__creates_new_entry(tmp_path):
    mm = Mindmap()
    result = mm.add_style("MyStyle", {"color": "#123456", "fontname": "Arial", "fontsize": "14"})
    assert result is True

    # Stelle sicher, dass der Style wirklich im XML existiert
    xml_entry = mm._mindmap.find('.//stylenode[@TEXT="MyStyle"]')
    assert xml_entry is not None
    assert xml_entry.get("COLOR") == "#123456"
    font_el = xml_entry.find("font")
    assert font_el is not None
    assert font_el.get("NAME") == "Arial"
    assert font_el.get("SIZE") == "14"

    # Doppelt hinzufügen -> False
    # result2 = mm.add_style("MyStyle", {"color": "#000000"})
    # assert result2 is False


def test__find_nodes__returns_node_instances(monkeypatch):
    mm = Mindmap()

    fake_xml_node = ET.Element("node", TEXT="Fake")
    monkeypatch.setattr(
        "freeplane.reduce_node_list", lambda **kw: [fake_xml_node]
    )

    result = mm.find_nodes(core="Fake")
    assert len(result) == 1
    assert isinstance(result[0], Node)
    assert result[0]._node is fake_xml_node
    assert result[0]._map is mm


def test__save__creates_valid_xml_file(tmp_path):
    mm = Mindmap()
    file_path = tmp_path / "test_output.mm"

    # Mock Encoding-Funktion
    import freeplane
    monkeypatch = pytest.MonkeyPatch()
    monkeypatch.setattr(freeplane, "get_version_specific_file_encoding", lambda v: "utf-8")

    mm.save(str(file_path))
    monkeypatch.undo()

    assert file_path.exists()
    content = file_path.read_text(encoding="utf-8")
    assert content.startswith("<map")
    assert "<node" in content


# def test_load_package_if_exists(tmp_path, caplog):
#     # Erzeuge temporäres Python-Modul
#     module_path = tmp_path / "mymodule.py"
#     module_path.write_text("x = 42")
#
#     # Führe Methode aus
#     mm = Mindmap()
#     import sys
#     old_dir = os.getcwd()
#     try:
#         os.chdir(tmp_path)
#         mm._load_package_if_exists("mymodule")
#         assert "mymodule" in globals()
#         assert "mymodule" in sys.modules
#         assert sys.modules["mymodule"].x == 42
#     finally:
#         os.chdir(old_dir)
