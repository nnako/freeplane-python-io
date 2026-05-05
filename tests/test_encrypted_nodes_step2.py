import pytest

from freeplane import Mindmap


def test__mindmap_manages_preferred_passwords_in_order():
    """Verify ordered password storage without duplicates."""
    mindmap = Mindmap()

    mindmap.add_password("alpha")
    mindmap.add_password("beta")
    mindmap.add_password("alpha")

    assert mindmap.passwords == ["alpha", "beta"]


def test__mindmap_can_replace_and_clear_passwords():
    """Verify password replacement and reset helpers."""
    mindmap = Mindmap()

    mindmap.set_passwords(["alpha", "beta", "alpha"])
    assert mindmap.passwords == ["alpha", "beta"]

    mindmap.clear_passwords()
    assert mindmap.passwords == []


def test__mindmap_prefers_explicit_password_then_first_map_password():
    """Verify password resolution for later encryption operations."""
    mindmap = Mindmap()
    mindmap.set_passwords(["alpha", "beta"])

    assert mindmap._get_effective_password("override") == "override"
    assert mindmap._get_effective_password() == "alpha"


def test__mindmap_requires_password_for_encryption_operations():
    """Verify missing passwords are rejected early."""
    mindmap = Mindmap()

    with pytest.raises(ValueError):
        mindmap._get_effective_password()
