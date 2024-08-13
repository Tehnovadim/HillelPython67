class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        if book not in self.books:
            self.books.append(book)
            return f"'{book.title}' has been added to the library."
        return f"'{book.title}' is already in the library."

    def remove_book(self, book: Book):
        if book in self.books:
            self.books.remove(book)
            return f"'{book.title}' has been removed from the library."
        return f"'{book.title}' is not in the library."

    def list_books(self):
        if not self.books:
            return "The library is empty."
        return "\n".join(str(book) for book in self.books)
