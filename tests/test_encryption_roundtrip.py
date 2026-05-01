import lxml.etree as ET

from encryption import PBEWithMD5AndDES


def test__encrypt_returns_freeplane_payload_and_roundtrips():
    cipher = PBEWithMD5AndDES()
    plain_text = '<node TEXT="roundtrip"><node TEXT="child"/></node>'

    encrypted_text = cipher.encrypt(plain_text, "test")
    decrypted_text = cipher.decrypt(encrypted_text, "test")

    assert " " in encrypted_text
    assert decrypted_text == plain_text


def test__encrypt_subtree_returns_encrypted_xml_structure():
    cipher = PBEWithMD5AndDES()
    subtree = ET.fromstring(
        """
        <node TEXT="parent" ID="ID_1" CREATED="1" MODIFIED="2">
          <attribute NAME="type" VALUE="test"/>
          <node TEXT="child"/>
        </node>
        """
    )

    encrypted_node = cipher.encrypt_subtree(subtree, "test")
    decrypted_node = cipher.decrypt_subtree(encrypted_node, "test")

    assert encrypted_node.tag == "node"
    assert encrypted_node.get("TEXT") == "parent"
    assert encrypted_node.get("ENCRYPTED_CONTENT")
    assert encrypted_node.findall("./node") == []
    assert encrypted_node.findall("./attribute") == []

    assert ET.tostring(decrypted_node) == ET.tostring(subtree)
