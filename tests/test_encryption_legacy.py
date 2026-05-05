import lxml.etree as ET

from encryption import PBEWithMD5AndDES


LEGACY_FREEPLANE_ENCRYPTED_CONTENT = (
    "U6aIS6sBnVs= "
    "0ztnLijlRVkEjD4seNID9ElgA94rMvxQ5wVbJFkEhzwHNYyiADeEY5pUXFjvbf7wSig9t8AIs/o5g6RKTy64TbXAXYlhJV44iNitZA5d3krnb+neBqitcmj6ARRyWb1IUMKXI4w5EamB+BLgaoon7Rc/YJrS4IlQSaOOsXGCvUKdBej0A3NxIl+w6tWNmoYf4ctJChtGYfQg/duG0uu4tWlry+GOhp4PaQzTCC1zVNKSMs+yCKrL72xETQl+7M/bVW3puBwbMp+Dx7Q8LURPo2pPs0kbzaossG8qieZAFPq7wLfI8xTfvXxcy0+C4V9/5w96YA+fSOnLfoAACYXKzl/SxBE7PKUBU6aSp9fTO7+GFMWjS0gUUGm3QOsZhvEBMmR1Xc1YmffFT0K/CzrU/4kjbi3Xdxk8DddUYQfAA6AijVNR1ZwAjYlh7lIROFRwh8ghjqj4xsyDa/Dre8dYByYNe1rDF+6dm2FUcuXBq5RRJAtTbeiT1Et/RrOvyKMe4B96iCna+NqDGrTMshDrEqIy57uCNFWH7RbGoYslH0OCO+UnE6SLick/s3JRjHR4IlNFZ7LpQAe0EWSCPj9/fL3IPFyuKaD6qC9h8CsVW1kPCWH2FZPTeJlzRA0smGxpJ+i2hITgyQUJQo2ndBvv1EImHbihYuo2u+PPk1Jim3h4ZXu/pdgICV0uPr3D4txuGVe4gh9qw++l61dZTYZy57HBjiH/AZ8hU+pfP9lwTs6BQyNXZ47arF6Q3AkjbxS0W5R8KXA70gIF5+GD+Wdu6eFdxyMBiOiq864Xf2aCk/coNsziiAWaZyL9fp3yTRpfnkVPAwYQxtFMNEhS4+GlbA=="
)


def test__pbewithmd5anddes_decrypts_legacy_freeplane_content():
    decrypted = PBEWithMD5AndDES().decrypt(
        LEGACY_FREEPLANE_ENCRYPTED_CONTENT,
        "test",
    )

    node = ET.fromstring(decrypted.encode("utf-8"))

    assert node.tag == "node"
    assert node.get("TEXT") == "this is an attributed node with HTML content"
    assert node.find('./attribute[@NAME="type"]').get("VALUE") == "test"
    assert [child.get("TEXT") for child in node.findall("./node")] == [
        "erster Child",
        None,
        "dritter Child",
    ]
