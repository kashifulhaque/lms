from models.book import Book
from storage import Storage

class BookService:
  _instance = None

  def __new__(cls, *args, **kwargs):
    if not cls._instance:
      cls._instance = super(BookService, cls).__new__(cls, *args, **kwargs)
    
    return cls._instance

  def __init__(self):
    self.storage = Storage('books.csv')
    self.books = self.storage.load()
  
  def add_book(self, title, author, isbn):
    book = Book(title, author, isbn)
    self.books.append(book)
    self.storage.save(self.books)
  
  def list_books(self):
    for book in self.books:
      print(book)
  
  def update_book(self, isbn, title=None, author=None):
    for book in self.books:
      if book.isbn == isbn:
        if title:
          book.title = title
        
        if author:
          book.author = author
        
        self.storage.save(self.books)
        return
    
    print(f"Book with ISBN: {isbn} not found")

  def delete_book(self, isbn):
    self.books = [book for book in self.books if book.isbn != isbn]
    self.storage.save(self.books)
  
  def search_books(self, title=None, author=None, isbn=None):
    results = []

    for book in self.books:
      if title and title in book.title:
        results.append(book)

      if author and author in book.author:
        results.append(book)

      if isbn and isbn == book.isbn:
        results.append(book)
    
    return results
