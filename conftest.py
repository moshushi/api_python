"""
Файл с фикстурами на проекте
"""
import pytest

from src.account import Account


@pytest.fixture(scope="module")
def default_account():
    account = Account("Nakamoto", 0)
    yield account
    del account
