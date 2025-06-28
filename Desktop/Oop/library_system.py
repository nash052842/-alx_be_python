# Base class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

# Derived class - EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size  # in MB

# Derived class - PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

# Composition - Library class
class Library:
    def __init__(self):
        self.books = []  # Holds instances of Book, EBook, or PrintBook

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            if isinstance(book, EBook):
                print(f"EBook: '{book.title}' by {book.author} - {book.file_size}MB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: '{book.title}' by {book.author} - {book.page_count} pages")
            else:
                print(f"Book: '{book.title}' by {book.author}")



# Base class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

# Derived class - EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size  # in MB

# Derived class - PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

# Composition - Library class
class Library:
    def __init__(self):
        self.books = []  # Holds instances of Book, EBook, or PrintBook

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            if isinstance(book, EBook):
                print(f"EBook: '{book.title}' by {book.author} - {book.file_size}MB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: '{book.title}' by {book.author} - {book.page_count} pages")
            else:
                print(f"Book: '{book.title}' by {book.author}")
