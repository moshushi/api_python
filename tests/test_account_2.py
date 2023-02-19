"""
Проверяем корректность создания аккаунта
"""
import pytest

from src.account import Account


@pytest.fixture
def default_account():
    account = Account("Nakamoto", 10)
    yield account
    del account


def test_account_deposite_balance(default_account):
    """
    Проверка баланса счёта
    :return:
    """
    default_account.deposit(100)
    assert default_account.balance == 100


def test_account_create_balance(default_account):
    """
    Проверка баланса счёта
    :return:
    """
    assert default_account.balance == 0
