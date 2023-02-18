"""
Модуль показывающий, как инициализируются классы
"""


class Book:
    """
    Класс книга, которая умеет открываться
    """
    cover_status = 'Close'

    def __init__(self, author, pages):
        self.author = author
        self.pages = pages

    def open_book(self):
        """
        Открываем книгу
        :return: Выводит на печать открытие книги
        """
        self.cover_status = "Open"
        print(f"Cover of the {self.author}'s book is opening...")

    def close_book(self):
        """
        Закрываем книгу
        :return: Выводит на печать закрытие книги
        """
        self.cover_status = "Close"
        print(f"Cover of the {self.author}'s book is closing...")


war_and_peace = Book(author='Tolstoy', pages=1000)
war_and_peace.supercover = 'Yes'

print(war_and_peace.supercover)
print(war_and_peace.cover_status)

war_and_peace.close_book()
