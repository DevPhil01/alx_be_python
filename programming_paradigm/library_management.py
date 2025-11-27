# library_management.py

class Book:
    """Represents a book in the library with title, author, and checkout status."""
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        # Private attribute to track availability
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False  # Already checked out

    def return_book(self):
        """Mark the book as returned (available again)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False  # Was not checked out

    def is_available(self):
        """Return True if the book is available, False if checked out."""
        return not self._is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    """Manages a collection of Book objects."""
    
    def __init__(self):
        # Private list to store books
        self._books = []

    def add_book(self, book):
        """Add a Book instance to the library."""
        if isinstance(book, Book):
            self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title if it exists and is available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False  # Book not found or already checked out

    def return_book(self, title):
        """Return a checked-out book by title."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        return False  # Book not found or not checked out

    def list_available_books(self):
        """Print all available (not checked out) books."""
        available_books = [book for book in self._books if book.is_available()]
        
        if not available_books:
            print("No books available.")
        else:
            for book in available_books:
                print(str(book))
