import pytest
import lxml.etree as ET
from unittest.mock import Mock, patch
import freeplane
from freeplane import Mindmap, Node


@pytest.fixture
def mindmap():
    """Eine einfache Mindmap-Instanz."""
    return Mindmap()


@pytest.fixture
def xmlNode():
    """
    Erstellt ein einfaches XML-Element, das eine Freeplane-Node repräsentiert.
    Dieses Element dient als Basis für viele Node-Tests.
    """
    return ET.Element("node", ID="ID_250101", TEXT="this is a node")


@pytest.fixture
def xml_node_with_image():
    """
    Erstellt eine Node mit einem Hook-Element für Tests von imagepath/imagesize.
    """
    xmlNode = ET.Element("node", ID="ID_IMG", TEXT="Node mit Bild")
    hook = ET.Element(
        "hook",
        URI="file:///C:/temp/image.png",
        SIZE="1",
        NAME="ExternalObject"
    )
    xmlNode.append(hook)
    return xmlNode


@pytest.fixture
def xml_node_with_attributes():
    """
    Erstellt eine Node mit mehreren Attribut-Elementen.
    """
    xmlNode = ET.Element("node", ID="ID_ATTR", TEXT="Node mit Attributen")
    attrs = [
        ET.Element("attribute", NAME="color", VALUE="blue"),
        ET.Element("attribute", NAME="shape", VALUE="square")
    ]
    for a in attrs:
        xmlNode.append(a)
    return xmlNode



@pytest.fixture
def mock_map():
    """
    Mock-Objekt für die Mindmap-Struktur. Simuliert Methoden wie find_nodes().
    """
    m = Mock()
    m._rootnode = None
    m._parentmap = {}
    m.styles = {"Standard": {}, "Header": {}}
    m.find_nodes = Mock(return_value=[])
    m._root = ET.Element("map")
    return m


@pytest.fixture
def fpNode(xmlNode, mock_map):
    """
    Standard-Node-Instanz, basierend auf xmlNode und mock_map.
    """
    return Node(xmlNode, mock_map)


@pytest.fixture
def node_with_image(xml_node_with_image, mock_map):
    """
    Node-Instanz mit eingebettetem Bild-Hook.
    """
    return Node(xml_node_with_image, mock_map)


@pytest.fixture
def node_with_attributes(xml_node_with_attributes, mock_map):
    """
    Node-Instanz mit vordefinierten XML-Attributen.
    """
    return Node(xml_node_with_attributes, mock_map)


@pytest.fixture
def linked_node(mock_map):
    """
    Separate Node, um Hyperlink- und Corelink-Referenzen zu simulieren.
    """
    linked_node_el = ET.Element("node", ID="ID_999", TEXT="Linked text")
    linked = Node(linked_node_el, mock_map)
    mock_map.find_nodes.return_value = [linked]
    return linked
