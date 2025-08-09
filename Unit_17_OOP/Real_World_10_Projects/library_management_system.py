class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False 

    def borrow(self):
        if self.is_borrowed:
            print(f"Sorry, '{self.title} is already borrowed.'")
            return False
        else:
            self.is_borrowed = True
            print(f"You borrowed '{self.title}'.")
            return True
        
    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"You returned '{self.title}'.")

        else:
            print(f"'{self.title}' was not borrowed.")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        print(f"Added book: '{book.title}' by {book.author}")

    def list_books(self):
        print("Available books:")
        for book in self.books:
            status = "Borrowed" if book.is_borrowed else "Available"
            print(f"{book.book_id}: {book.title} by {book.author} - {status}")

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
            
        print(f"Book '{title}' not found.")
        return None
    

library = Library()

library.add_book(Book(1, "The Alchemist", "Paulo Coelho"))
library.add_book(Book(2, "1984", "George Orwell"))
library.add_book(Book(3, "To Kill a Mockingbird", "Harper Lee"))

library.list_books()

book = library.find_book("1984")
if book:
    book.borrow()

    library.list_books()

    book.return_book()

    library.list_books()

