from models.book import Book
from storage import Storage

from thefuzz import fuzz

# BookService class handles operations related to books
class BookService:
  _instance = None

  def __new__(cls, *args, **kwargs):
    if not cls._instance:
      cls._instance = super(BookService, cls).__new__(cls, *args, **kwargs)
    
    return cls._instance

  def __init__(self):
    self.storage = Storage('books.csv')
    self.books = self.storage.load()
  
  # Add a book to the library
  def add_book(self, title, author, isbn):
    book = Book(title, author, isbn)

    for ele in self.books:
      if ele == book:
        return False

    self.books.append(book)
    self.storage.save(self.books)
    self.__init__()
    return True
  
  # List all books in the library
  def list_books(self):
    for book in self.books:
      print(book)

  # Update book details in the library
  def update_book(self, isbn, title = None, author = None):
    for book in self.books:
      if book.isbn == isbn:
        if title:
          book.title = title
        
        if author:
          book.author = author
        
        self.storage.save(self.books)
        self.__init()
        return
    
    print(f"Book with ISBN: {isbn} not found")

  # Delete a book from the library
  def delete_book(self, isbn):
    self.books = [book for book in self.books if book.isbn != isbn]
    self.storage.save(self.books)
    self.__init__()

  # Search for a book by ISBN
  def search_book_by_isbn(self, isbn):
    results = []

    for book in self.books:
      if isbn and isbn == book.isbn:
        results.append(book)
    
    return results

  # Search for books by title
  def search_book_by_title(self, title):
    results = []
    
    for book in self.books:
      ratio = fuzz.token_set_ratio(title, book.title)

      if title and ratio >= 50:
        results.append(book)

    return results

  # Search for books by author
  def search_book_by_author(self, author):
    results = []
    
    for book in self.books:
      ratio = fuzz.token_set_ratio(author, book.author)

      if author and ratio >= 50:
        results.append(book)

    return results
