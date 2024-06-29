class Book:
  def __init__(self, title, author, isbn):
    self.title = title
    self.author = author
    self.isbn = isbn
    self.is_checked_out = False
  
  def __repr__(self):
    return f"Book(title = {self.title}, author = {self.author}, isbn = {self.isbn}, is_checked_out = {self.is_checked_out})"
