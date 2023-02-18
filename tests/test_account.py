"""
Проверяем корректность создания аккаунта
"""
import pytest

from src.account import Account


@pytest.fixture
def default_account():
    return Account("Nakamoto", 0)


def tear_down(account):
    del account


def test_account_create_balance(default_account):
    """
    Проверка баланса счёта
    :return:
    """
    assert default_account.balance == 0
    # del default_account


def test_account_create_name(default_account):
    """
    Проверка баланса счёта
    :return:
    """
    assert default_account.owner == "Nakamoto"
    # del default_account
