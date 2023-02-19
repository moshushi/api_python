"""
Проверяем корректность создания аккаунта
"""


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
