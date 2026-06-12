import pytest
import os
from app.main import somar, subtrair, obter_api_key


def test_somar():
    assert somar(2, 3) == 5
    assert somar(-1, 1) == 0


def test_subtrair():
    assert subtrair(10, 4) == 6
    assert subtrair(0, 5) == -5


def test_obter_api_key_sucesso(monkeypatch):
    monkeypatch.setenv("MINHA_API_SECRET", "token-de-teste")
    assert obter_api_key() == "token-de-teste"


def test_obter_api_key_ausente(monkeypatch):
    monkeypatch.delenv("MINHA_API_SECRET", raising=False)
    with pytest.raises(ValueError):
        obter_api_key()