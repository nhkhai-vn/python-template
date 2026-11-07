import sys

import pytest

from app.__main__ import main


def test_prints_greeting(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    monkeypatch.setattr(sys, "argv", ["app", "Khai"])
    main()
    assert capsys.readouterr().out == "Hello, Khai!\n"


def test_defaults_to_world(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    monkeypatch.setattr(sys, "argv", ["app"])
    main()
    assert capsys.readouterr().out == "Hello, world!\n"
