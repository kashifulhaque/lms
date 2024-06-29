class Book:
  def __init__(self, title, author, isbn):
    self.title = title
    self.author = author
    self.isbn = isbn
  
  def __repr__(self):
    return f"----------------\nISBN: {self.isbn}\n{self.title}, authored by {self.author}"
  
  def __eq__(self, other):
    if not isinstance(other, Book):
      return False
    
    return self.isbn == other.isbn

  def __hash__(self):
    return self.isbn
