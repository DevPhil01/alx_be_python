# book_class.py

class Book:
    """
    A simple class representing a book with title, author, and publication year.
    Implements constructor, destructor, and representation magic methods.
    """
    
    def __init__(self, title: str, author: str, year: int):
        """
        Initialize a new Book instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            year (int): The publication year
        """
        self.title = title
        self.author = author
        self.year = year
    
    def __str__(self) -> str:
        """
        Return a human-readable string representation of the book.
        Used by print() and str().
        
        Returns:
            str: Formatted string like "1984 by George Orwell, published in 1949"
        """
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self) -> str:
        """
        Return an official string representation that could recreate the object.
        Used by repr() and in debugging.
        
        Returns:
            str: String that looks like a constructor call
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
    
    def __del__(self):
        """
        Destructor method called when the Book instance is about to be destroyed.
        Prints a message indicating the book is being deleted.
        """
        print(f"Deleting {self.title}")
