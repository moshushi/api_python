"""
Проверяем корректность создания аккаунта
"""
from src.account import Account


def test_account_create_balance():
    """
    Проверка баланса счёта
    :return:
    """
    a = Account("Nakamoto", 0)
    assert a.balance == 0
    del a


def test_account_create_name():
    """
    Проверка баланса счёта
    :return:
    """
    a = Account("Nakamoto", 0)
    assert a.owner == "Nakamoto"
    del a
