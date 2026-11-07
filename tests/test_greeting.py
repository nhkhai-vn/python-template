import pytest

from app.greeting import greet


def test_greets_by_name() -> None:
    assert greet("Khai") == "Hello, Khai!"


def test_strips_whitespace() -> None:
    assert greet("  Khai ") == "Hello, Khai!"


@pytest.mark.parametrize("name", ["", "   "])
def test_rejects_empty_name(name: str) -> None:
    with pytest.raises(ValueError, match="name is empty"):
        greet(name)
