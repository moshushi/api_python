"""
Модуль показывает инкапсуляцию (сокрытие) свойств класса
"""


class Book:
    """
    Класс создающий абстрактную книгу
    """
    __cover_status = 'Close'

    def __init__(self, author, pages):
        self.author = author
        self.pages = pages

    def open_book(self):
        """
        Метод открывающий книгу
        :return: Печатает вывод
        """
        self.__cover_status = "Open"
        print(f"Cover of the {self.author}'s book is opening...")

    def close_book(self):
        """
        Метод закрывающий книгу
        :return: Печатает вывод
        """
        self.__cover_status = "Close"
        print(f"Cover of the {self.author}'s book is closing...")


war_and_peace = Book(author='Tolstoy', pages=1000)

# print(war_and_peace.__cover_status)

war_and_peace.close_book()
