import datetime
import lxml.etree as ET
import pytest
from types import SimpleNamespace
from unittest.mock import Mock, patch

import freeplane
from freeplane import Node, Mindmap


# @pytest.fixture(autouse=True)
# def reset_globals():
#     Mindmap._num_of_maps = 0
#     Mindmap._global_node_id_incr = 0
#     Mindmap._global_node_id_seed = "250101"



# @pytest.fixture
# def fpNode(xmlNode, mindmap, monkeypatch):
#     """Eine Node-Instanz mit gemockten Abhängigkeiten."""
#     monkeypatch.setattr("freeplane.update_date_attribute_in_node", lambda **kw: None)
#     monkeypatch.setattr("freeplane.getCoreTextFromNode", lambda node, bOnlyFirstLine=False: node.attrib.get("TEXT", ""))
#     monkeypatch.setattr("freeplane.sanitized", lambda s: s)
#     return Node(xmlNode, mindmap)


#
# TESTS
#


#
#
#

def test__init__creates_node_with_id(xmlNode, mindmap, monkeypatch):
    fpNode = Node(xmlNode, mindmap)
    assert hasattr(fpNode, "id")
    assert fpNode.id.startswith("ID_250101")


def test__repr__returns_plaintext(fpNode):
    assert str(fpNode) == fpNode.plaintext
    assert repr(fpNode) == fpNode.plaintext


def test__is_root_node__true_for_rootnode(mindmap):
    fpNode = Node(mindmap._rootnode, mindmap)
    assert fpNode.is_root_node is True


def test__is_map_node__true_for_non_rootnode(mindmap):
    xmlnode = ET.Element("node", {"TEXT": "Child"})
    fpNode = Node(xmlnode, mindmap)
    assert fpNode.is_map_node is True


def test__is_detached_head_and_node(monkeypatch, xmlNode):
    fake_branch = SimpleNamespace(_parentmap={})
    fpNode = Node(xmlNode, None)
    fpNode._branch = fake_branch

    # Detached head: node not in parentmap
    assert fpNode.is_detached_head is True
    # Detached node: when node is in parentmap
    fpNode._branch._parentmap[xmlNode] = "dummy"
    assert fpNode.is_detached_node is True


def test__plaintext__returns_text(fpNode):
    assert fpNode.plaintext == "this is a node"


def test__plaintext__setter_removes_richcontent(fpNode):
    rc = ET.SubElement(fpNode._node, "richcontent")
    fpNode.plaintext = "New text"
    assert fpNode._node.attrib["TEXT"] == "New text"
    assert fpNode._node.find("richcontent") is None


def test__hyperlink__setter_and_getter(fpNode, monkeypatch):
    fpNode._node.attrib["LINK"] = "#TargetNode"
    assert fpNode.hyperlink == "#TargetNode"


def test__has_internal_hyperlink__detects_hash_link(fpNode):
    fpNode._node.attrib["LINK"] = "#SOME_ID"
    assert fpNode.has_internal_hyperlink is True
    fpNode._node.attrib["LINK"] = "http://example.com"
    assert fpNode.has_internal_hyperlink is False


def test__follow_internal_hyperlink__returns_new_node(monkeypatch, mindmap):
    xmlTargetNode = ET.Element("node", {"ID": "TARGET", "TEXT": "Target"})
    fpTargetNode = Node(xmlTargetNode, mindmap)

    # monkey patch find_nodes function to return exactly one hit: the target
    # fpNode which is searched for by the user
    monkeypatch.setattr("freeplane.Node", Node)
    monkeypatch.setattr("freeplane.Mindmap.find_nodes", lambda self, **kw: [fpTargetNode])

    xmlNode = ET.Element("node", {"LINK": "#TARGET", "TEXT": "Source"})
    source_node = Node(xmlNode, mindmap)

    result = source_node.follow_internal_hyperlink
    assert isinstance(result, Node)
    assert result._node.attrib["TEXT"] == "Target"


def test__follow_corelink__returns_new_node(monkeypatch, mindmap):
    xmlTargetNode = ET.Element("node", {"ID": "X42", "TEXT": "Remote"})
    fpTargetNode = Node(xmlTargetNode, mindmap)

    # monkey patch find_nodes function to return exactly one hit: the target
    # fpNode which is searched for by the user
    monkeypatch.setattr("freeplane.Node", Node)
    monkeypatch.setattr("freeplane.Mindmap.find_nodes", lambda self, **kw: [fpTargetNode])

    # add core link
    n = Node(ET.Element("node", {"TEXT": "=X42.text"}), mindmap)
    # n.corelink = "X42"

    # simulate property by direct assignment
    monkeypatch.setattr(Node, "corelink", property(lambda self: "X42"))

    result = n.follow_corelink
    assert isinstance(result, Node)
    assert result._node.attrib["TEXT"] == "Remote"


def test__visibletext__uses_corelink(monkeypatch, mindmap):
    linked_node = Node(ET.Element("node", {"ID": "ID_X", "TEXT": "Linked"}), mindmap)
    monkeypatch.setattr("freeplane.Mindmap.find_nodes", lambda self, **kw: [linked_node])
    fpNode = Node(ET.Element("node", {"TEXT": "Local"}), mindmap)
    monkeypatch.setattr(Node, "corelink", property(lambda self: "ID_X"))
    assert fpNode.visibletext == "Linked"


def test__visibletext__returns_plaintext_when_no_corelink(fpNode):
    assert fpNode.visibletext == "Hello"


# --------------------------------------------------------------------------- #
# ID PROPERTY
# --------------------------------------------------------------------------- #

def test__id__getter_returns_id(fpNode):
    assert fpNode.id.startswith("ID_250101")


def test__id__shows_valid_format(fpNode):
    # start with "ID_" token
    assert fpNode.id.startswith("ID_")
    # only numbers behind token
    assert fpNode.id[2:].isnumeric() is False


# def test__id__setter_corrects_and_rejects_invalid_format(fpNode, caplog):
#     ok = fpNode.id = "12345"
#     assert fpNode.id == "ID_12345"
#     ok2 = fpNode.id = "ID_abc"
#     assert ok2 is False


# --------------------------------------------------------------------------- #
# IMAGEPATH / IMAGESIZE / SET_IMAGE
# --------------------------------------------------------------------------- #

def test__imagepath__returns_clean_path(fpNode, monkeypatch):
    hook = ET.SubElement(fpNode._node, "hook", URI="file:///C:/Images/pic.png", NAME="ExternalObject")
    path = fpNode.imagepath
    assert path == "C:/Images/pic.png"


# def test__imagepath__returns_none_when_no_hook(fpNode, caplog):
#     result = fpNode.imagepath
#     assert result is None
    # assert "does not contain an in-line image" in caplog.text


def test__imagesize__returns_value(fpNode):
    hook = ET.SubElement(fpNode._node, "hook", SIZE="0.8", NAME="ExternalObject")
    assert fpNode.imagesize == "0.8"


# def test__imagesize__returns_none_when_no_hook(fpNode):
#     assert fpNode.imagesize is None


@pytest.mark.parametrize(
    "link,expected_uri",
    [
        ("/home/user/pic.png", "file:///home/user/pic.png"),
        ("C:/Images/pic.png", "file:///C:/Images/pic.png"),
        ("./relpath/pic.png", "./relpath/pic.png"),
        ("https://example.com/pic.png", "https://example.com/pic.png"),
        ("image.png", "./image.png"),
    ],
)
def test__set_image__creates_or_updates_hook(fpNode, link, expected_uri):
    ok = fpNode.set_image(link=link, size="2")
    assert ok is True
    hook = fpNode._node.find("hook")
    assert hook is not None
    assert hook.get("URI") == expected_uri
    assert hook.get("SIZE") == "2"


# --------------------------------------------------------------------------- #
# ATTRIBUTES
# --------------------------------------------------------------------------- #

def test__attributes__returns_dict(fpNode):
    ET.SubElement(fpNode._node, "attribute", NAME="color", VALUE="red")
    ET.SubElement(fpNode._node, "attribute", NAME="size", VALUE="XL")
    attrs = fpNode.attributes
    assert attrs == {"color": "red", "size": "XL"}


def test__set_attribute__adds_new_attribute(fpNode):
    fpNode.set_attribute("theme", "dark")
    attrs = fpNode.attributes
    assert attrs == {"theme": "dark"}


def test__set_attribute__overwrites_existing_value(fpNode):
    ET.SubElement(fpNode._node, "attribute", NAME="priority", VALUE="low")
    fpNode.set_attribute("priority", "high")
    attrs = fpNode.attributes
    assert attrs["priority"] == "high"


def test__remove_attribute__removes_existing(fpNode):
    ET.SubElement(fpNode._node, "attribute", NAME="status", VALUE="todo")
    result = fpNode.remove_attribute("status")
    assert result is True
    assert fpNode.attributes == {}


def test__remove_attribute__returns_false_if_missing(fpNode):
    result = fpNode.remove_attribute("not_existing")
    assert result is False


def test__add_attribute__creates_new_element(fpNode):
    fpNode.add_attribute("owner", "me")
    attrs = fpNode.attributes
    assert "owner" in attrs
    assert attrs["owner"] == "me"


#
#
#

def test__style__getter_and_setter(xmlNode, mock_map):
    fpNode = Node(xmlNode, mock_map)

    # initially no style
    assert fpNode.style == ""

    # set valid style
    fpNode.style = "Header"
    assert xmlNode.attrib["STYLE_REF"] == "Header"

    # set empty style (removes attribute)
    fpNode.style = ""
    assert "STYLE_REF" not in xmlNode.attrib

    # invalid style triggers warning but still sets
    fpNode._map.styles = {"Standard": {}}
    fpNode.style = "UnknownStyle"
    assert xmlNode.attrib["STYLE_REF"] == "UnknownStyle"


def test__creation_and_modification_dates(xmlNode, mock_map):
    fpNode = Node(xmlNode, mock_map)
    now = datetime.datetime.now().timestamp() * 1000
    xmlNode.set("CREATED", str(now))
    xmlNode.set("MODIFIED", str(now))

    created = fpNode.creationdate
    modified = fpNode.modificationdate

    assert isinstance(created, tuple)
    assert isinstance(modified, tuple)
    assert created.tm_year >= 1970


def test__corelink__detects_internal_reference(xmlNode, mock_map, monkeypatch):
    fpNode = Node(xmlNode, mock_map)
    # simulate plaintext property
    monkeypatch.setattr(Node, "plaintext", "=ID_123.text something")
    assert fpNode.corelink == "ID_123"

    # no match
    monkeypatch.setattr(Node, "plaintext", "normal text")
    assert fpNode.corelink == ""


def test__comment_property(xmlNode, mock_map):
    child = ET.SubElement(xmlNode, "node", TEXT="Child comment")
    fpNode = Node(xmlNode, mock_map)
    assert fpNode.comment == "Child comment"

    xmlNode.remove(child)
    assert fpNode.comment == ""


def test__details__getter_and_setter(xmlNode, mock_map):
    fpNode = Node(xmlNode, mock_map)

    # initially empty
    assert fpNode.details == ""

    # set details
    fpNode.details = "Line 1\nLine 2"
    details_node = xmlNode.find("./richcontent[@TYPE='DETAILS']")
    assert details_node is not None
    assert "Line 1" in ''.join(details_node.itertext())

    # overwrite with new text
    fpNode.details = "New text"
    assert "New text" in ''.join(xmlNode.find("./richcontent[@TYPE='DETAILS']").itertext())

    # remove details
    fpNode.details = ""
    assert xmlNode.find("./richcontent[@TYPE='DETAILS']") is None


def test__notes__getter_and_setter(xmlNode, mock_map):
    fpNode = Node(xmlNode, mock_map)

    fpNode.notes = "Hello\nWorld"
    assert fpNode.notes == "Hello\nWorld"

    fpNode.notes = ""
    assert xmlNode.find("./richcontent[@TYPE='NOTE']") is None


def test__icons_add_and_del(xmlNode, mock_map):
    fpNode = Node(xmlNode, mock_map)
    fpNode.add_icon("idea")
    fpNode.add_icon("flag")
    assert "idea" in fpNode.icons
    assert "flag" in fpNode.icons

    fpNode.del_icon("idea")
    assert "idea" not in fpNode.icons


def test__add_and_remove_child(xmlNode, mock_map):
    mock_map._rootnode = xmlNode
    fpNode = Node(xmlNode, mock_map)
    child = fpNode.add_child(core="ChildText", id="ID_2")
    assert isinstance(child, Node)
    assert child._node.get("TEXT") == "ChildText"
    assert mock_map._parentmap[child._node] == xmlNode

    # remove it
    assert child.remove() is True
    assert child._node not in list(xmlNode)


def test__add_sibling(xmlNode, mock_map):
    mock_map._rootnode = xmlNode
    fpNode = Node(xmlNode, mock_map)

    parent = ET.Element("root")
    parent.append(xmlNode)

    fpNode._node = xmlNode
    fpNode._map._parentmap = {xmlNode: parent}

    sibling = fpNode.add_sibling(core="Brother", id="ID_3")
    assert sibling._node.get("TEXT") == "Brother"
    assert mock_map._parentmap[sibling._node] == parent


def test__arrowlink__add_and_del(xmlNode, mock_map):
    fpNode = Node(xmlNode, mock_map)
    target_node = Node(ET.Element("node", ID="ID_99"), mock_map)
    mock_map._root.append(target_node._node)

    fpNode.add_arrowlink(node=target_node, color="#FF0000", width="3")
    arrow = xmlNode.find("./arrowlink")
    assert arrow is not None
    assert arrow.attrib["DESTINATION"] == "ID_99"
    assert arrow.attrib["COLOR"] == "#FF0000"

    assert fpNode.del_arrowlink("ID_99") is True
    assert xmlNode.find("./arrowlink") is None


def test__arrowlinked_property(xmlNode, mock_map):
    target = Node(ET.Element("node", ID="ID_2"), mock_map)
    mock_map._root.append(xmlNode)
    mock_map._root.append(target._node)
    ET.SubElement(xmlNode, "arrowlink", DESTINATION="ID_2")

    assert target.arrowlinked[0].id == "ID_1"


def test__children_and_index(xmlNode, mock_map):
    mock_map._rootnode = xmlNode
    fpNode = Node(xmlNode, mock_map)
    for i in range(3):
        fpNode.add_child(core=f"child{i}", id=f"ID_{i+2}")

    assert len(fpNode.children) == 3
    assert fpNode.get_child_by_index(1).id == "ID_3"
    assert fpNode.get_child_by_index(5) is None


def test__is_rootnode_and_has_children(xmlNode, mock_map):
    mock_map._rootnode = xmlNode
    fpNode = Node(xmlNode, mock_map)
    assert fpNode.is_rootnode is True
    assert fpNode.has_children is False
    fpNode.add_child(core="X", id="ID_2")
    assert fpNode.has_children is True


# --------------------------------------------------------------------------- #
# ATTACH / DETACH
# --------------------------------------------------------------------------- #

# def test__attach__sets_branch_and_map_reference(fpNode):
#     branch = Mock()
#     branch._parentmap = {fpNode._node: None}
#     fpNode.attach(branch)
#     assert fpNode._branch == branch
#     assert fpNode._map is None


def test__is_descendant_of__returns_true_if_nested(fpNode):
    parent_node = ET.Element("node", ID="ID_PARENT", TEXT="Parent")
    parent = Node(parent_node, fpNode._map)
    parent._map._parentmap = {fpNode._node: parent_node}

    fpNode._map._parentmap = {fpNode._node: parent_node}
    assert fpNode.is_descendant_of(parent) is True


def test__is_descendant_of__returns_false_for_unrelated(fpNode):
    parent_node = ET.Element("node", ID="ID_PARENT", TEXT="Parent")
    parent = Node(parent_node, fpNode._map)
    fpNode._map._parentmap = {}
    assert fpNode.is_descendant_of(parent) is False


#
# indent chain management
#

def test__get_indexchain_until__returns_correct_chain(fpNode):

    # node structure
    #
    #  .-----------. .--------. .--------.
    #  | tree-root | | child1 | | child2 |
    #  '-----------' '--------' '--------'
    #
    child1 = ET.SubElement(fpNode._node, "node", ID="ID_2")
    child2 = ET.SubElement(child1, "node", ID="ID_3")

    # setup map element with tree-root as map's root
    map_mock = Mock()
    map_mock._parentmap = {child1: fpNode._node, child2: child1}
    map_mock._rootnode = fpNode._node

    # connect all nodes to map
    fpNode._map = map_mock
    n1 = Node(child1, map_mock)
    n2 = Node(child2, map_mock)

    chain = n2.get_indexchain_until(fpNode)
    assert isinstance(chain, list)
    assert chain == [0, 0]  # child1 index 0, child2 index 0


def test__get_indexchain_until__returns_empty_for_no_parent(fpNode):
    fpNode._map._parentmap = {}
    chain = fpNode.get_indexchain_until(fpNode)
    assert chain == []


# --------------------------------------------------------------------------- #
# FIND_NODES / FIND_CHILDREN
# --------------------------------------------------------------------------- #

def test__find_nodes__returns_if_contained_and_casesensitive_match(fpNode):
    # Build a mini tree
    ET.SubElement(fpNode._node, "node", ID="ID_2", TEXT="fOo")
    ET.SubElement(fpNode._node, "node", ID="ID_3", TEXT="bar")
    n2 = Node(fpNode._node[0], fpNode._map)
    n3 = Node(fpNode._node[1], fpNode._map)

    results = fpNode.find_nodes(core="fO")
    assert any(n.id == "ID_2" for n in results)
    assert all(isinstance(r, Node) for r in results)


def test__find_nodes__returns_if_exact_but_caseinsensitive_match(fpNode):
    # Build a mini tree
    ET.SubElement(fpNode._node, "node", ID="ID_2", TEXT="fOo")
    ET.SubElement(fpNode._node, "node", ID="ID_3", TEXT="bar")
    n2 = Node(fpNode._node[0], fpNode._map)
    n3 = Node(fpNode._node[1], fpNode._map)

    results = fpNode.find_nodes(core="foo", exact=True, caseinsensitive=True)
    assert any(n.id == "ID_2" for n in results)
    assert all(isinstance(r, Node) for r in results)


def test__find_nodes__returns_if_regex_matches(fpNode):
    # Build a mini tree
    ET.SubElement(fpNode._node, "node", ID="ID_2", TEXT="fooooo")
    ET.SubElement(fpNode._node, "node", ID="ID_3", TEXT="bar")
    n2 = Node(fpNode._node[0], fpNode._map)
    n3 = Node(fpNode._node[1], fpNode._map)

    results = fpNode.find_nodes(core=r"f[o]+", regex=True)
    assert any(n.id == "ID_2" for n in results)
    assert all(isinstance(r, Node) for r in results)


def test__find_nodes__returns_empty_if_not_found(fpNode):
    results = fpNode.find_nodes(core="xyz")
    assert results == []


def test__find_children__returns_direct_children(fpNode):
    c1 = ET.SubElement(fpNode._node, "node", ID="ID_2", TEXT="first")
    c2 = ET.SubElement(fpNode._node, "node", ID="ID_3", TEXT="second")
    fpNode._map._parentmap = {c1: fpNode._node, c2: fpNode._node}

    result = fpNode.find_children()
    assert len(result) == 2
    assert all(isinstance(r, Node) for r in result)


# --------------------------------------------------------------------------- #
# ADD_ARROWLINK – Erweiterte Varianten
# --------------------------------------------------------------------------- #

def test__add_arrowlink__creates_valid_element(fpNode):
    target_node = Node(ET.Element("node", ID="ID_99"), fpNode._map)
    fpNode.add_arrowlink(node=target_node, color="#123456", width="2", style="bezier")
    arrow = fpNode._node.find("./arrowlink")
    assert arrow is not None
    assert arrow.attrib["DESTINATION"] == "ID_99"
    assert arrow.attrib["STYLE"] == "bezier"


def test__add_arrowlink__handles_existing_link(fpNode):
    t = Node(ET.Element("node", ID="ID_5"), fpNode._map)
    fpNode.add_arrowlink(node=t)
    fpNode.add_arrowlink(node=t)  # should not duplicate
    arrows = fpNode._node.findall("./arrowlink")
    assert len(arrows) == 1


# --------------------------------------------------------------------------- #
# OTHER SMALL UTILITIES
# --------------------------------------------------------------------------- #

def test__get_parent__returns_correct_parent(fpNode):
    parent_el = ET.Element("node", ID="ID_PARENT")
    parent_el.append(fpNode._node)
    fpNode._map._parentmap = {fpNode._node: parent_el}
    parent_node = fpNode.get_parent()
    assert isinstance(parent_node, Node)
    assert parent_node.id == "ID_PARENT"


def test__get_parent__returns_none_for_detached(fpNode):
    fpNode._map._parentmap = {}
    assert fpNode.get_parent() is None


def test__index_in_parent__returns_position(fpNode):
    parent_el = ET.Element("node", ID="ID_PARENT")
    c1 = ET.SubElement(parent_el, "node", ID="ID_A")
    c2 = ET.SubElement(parent_el, "node", ID="ID_B")
    fpNode._node = c2
    fpNode._map._parentmap = {c1: parent_el, c2: parent_el}
    assert fpNode.index_in_parent == 1


def test__index_in_parent__returns_minus_one_for_root(fpNode):
    fpNode._map._rootnode = fpNode._node
    assert fpNode.index_in_parent == -1


# --------------------------------------------------------------------------- #
# PLAINTEXT & VISIBLETEXT
# --------------------------------------------------------------------------- #

@patch("freeplane.node.getCoreTextFromNode", return_value="Simple text")
@patch("freeplane.node.sanitized", side_effect=lambda x: x)
def test__plaintext__returns_sanitized_text(mock_sanitize, mock_coretext, fpNode):
    assert fpNode.plaintext == "Simple text"
    mock_coretext.assert_called_once()
    mock_sanitize.assert_called_once()


def test__visibletext__returns_plaintext_when_no_corelink(fpNode, monkeypatch):
    monkeypatch.setattr(Node, "corelink", "")
    monkeypatch.setattr(Node, "plaintext", "Visible text")
    assert fpNode.visibletext == "Visible text"


def test__visibletext__resolves_corelink_to_other_node(fpNode, mock_map, monkeypatch):
    linked_node_el = ET.Element("node", ID="ID_999", TEXT="Linked text")
    linked_node = Node(linked_node_el, mock_map)
    mock_map.find_nodes.return_value = [linked_node]
    monkeypatch.setattr(Node, "corelink", "ID_999")

    result = fpNode.visibletext
    assert result == linked_node.plaintext


# --------------------------------------------------------------------------- #
# HYPERLINK PROPERTY
# --------------------------------------------------------------------------- #

def test__hyperlink__getter_returns_value(fpNode):
    fpNode._node.set("LINK", "https://example.com")
    assert fpNode.hyperlink == "https://example.com"


@patch("freeplane.node.update_date_attribute_in_node")
def test__hyperlink__setter_sets_attribute(mock_update, fpNode):
    ok = fpNode.hyperlink = "https://new.example.com"
    assert fpNode._node.attrib["LINK"] == "https://new.example.com"
    assert ok is True
    mock_update.assert_called_once()


# --------------------------------------------------------------------------- #
# FOLLOW_INTERNAL_HYPERLINK
# --------------------------------------------------------------------------- #

def test__follow_internal_hyperlink__returns_target_node(fpNode, mock_map):
    mock_map.find_nodes.return_value = [Node(ET.Element("node", ID="ID_2"), mock_map)]
    fpNode._node.set("LINK", "#ID_2")
    result = fpNode.follow_internal_hyperlink
    assert isinstance(result, Node)
    assert result.id == "ID_2"


def test__follow_internal_hyperlink__returns_none_when_target_missing(fpNode, mock_map, caplog):
    mock_map.find_nodes.return_value = []
    fpNode._node.set("LINK", "#ID_XYZ")
    result = fpNode.follow_internal_hyperlink
    assert result is None
    assert "was not found" in caplog.text


def test__follow_internal_hyperlink__returns_none_if_not_internal(fpNode):
    fpNode._node.set("LINK", "https://example.com")
    assert fpNode.follow_internal_hyperlink is None


# --------------------------------------------------------------------------- #
# FOLLOW_CORELINK
# --------------------------------------------------------------------------- #

def test__follow_corelink__returns_target_node(fpNode, mock_map, monkeypatch):
    linked_node_el = ET.Element("node", ID="ID_ABC", TEXT="Linked")
    linked_node = Node(linked_node_el, mock_map)
    mock_map.find_nodes.return_value = [linked_node]
    monkeypatch.setattr(Node, "corelink", "ID_ABC")

    result = fpNode.follow_corelink
    assert isinstance(result, Node)
    assert result.id == "ID_ABC"


def test__follow_corelink__returns_none_if_target_not_found(fpNode, mock_map, monkeypatch, caplog):
    mock_map.find_nodes.return_value = []
    monkeypatch.setattr(Node, "corelink", "ID_MISSING")
    result = fpNode.follow_corelink
    assert result is None
    assert "was not found" in caplog.text


def test__follow_corelink__returns_none_if_no_corelink(fpNode, monkeypatch):
    monkeypatch.setattr(Node, "corelink", "")
    assert fpNode.follow_corelink is None


# --------------------------------------------------------------------------- #
# HAS_INTERNAL_HYPERLINK
# --------------------------------------------------------------------------- #

def test__has_internal_hyperlink__detects_hash_prefix(fpNode):
    fpNode._node.set("LINK", "#ID_123")
    assert fpNode.has_internal_hyperlink is True


def test__has_internal_hyperlink__returns_false_for_empty_or_external(fpNode):
    fpNode._node.attrib.pop("LINK", None)
    assert fpNode.has_internal_hyperlink is False
    fpNode._node.set("LINK", "http://example.com")
    assert fpNode.has_internal_hyperlink is False
