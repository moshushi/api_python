"""
Модуль создающий банковский аккаунт
"""
import uuid


class Account:
    """
    Создает банковский аккаунт физическому лицу
    """

    def __init__(self, name, balance=0):
        self.__uid = str(uuid.uuid4())
        self.__owner = name
        self.__balance = 0

    def put_money(self, x):
        """
        Внести деньги на баланс счёта
        :return:
        """
        self.__balance = x

    @property
    def balance(self):
        """
        Показать баланс на счету
        :return:
        """
        return (self.__balance)

    @property
    def owner(self):
        """
        Показать кому принадлежит счёт
        :return:
        """
        return (self.__owner)

    def __del__(self):
        print(f"Account {self.__owner} with {self.__balance} deleted")
        print(f'{self.__uid}')
