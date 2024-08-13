import pytest
from book_library import Book, Library

@pytest.fixture(scope='class')
def library():
    return Library()

@pytest.fixture(scope='class')
def book1():
    return Book(title="1984", author="George Orwell", year=1949)

@pytest.fixture(scope='class')
def book2():
    return Book(title="To Kill a Mockingbird", author="Harper Lee", year=1960)

@pytest.fixture(scope='class')
def book3():
    return Book(title="The Great Gatsby", author="F. Scott Fitzgerald", year=1925)

class TestLibrary:
    def test_add_book(self, library, book1, book2):
        assert library.add_book(book1) == "'1984' has been added to the library."
        assert library.add_book(book2) == "'To Kill a Mockingbird' has been added to the library."
        assert library.add_book(book1) == "'1984' is already in the library."

    def test_remove_book(self, library, book1, book3):
        assert library.remove_book(book3) == "'The Great Gatsby' is not in the library."
        assert library.remove_book(book1) == "'1984' has been removed from the library."
        assert library.remove_book(book1) == "'1984' is not in the library."

    def test_list_books(self, library, book2, book3):
        library.add_book(book2)
        library.add_book(book3)
        assert library.list_books() == "'To Kill a Mockingbird' by Harper Lee (1960)\n'The Great Gatsby' by F. Scott Fitzgerald (1925)"
