from freeplane import Mindmap


def test__mindmap_initializes_encryption_runtime_state():
    """Verify that a mindmap starts with empty encryption runtime helpers."""
    mindmap = Mindmap()

    assert mindmap._preferred_passwords == []
    assert mindmap._encrypted_nodes == {}
    assert mindmap._cipher is not None
