# Checkout class represents a checkout entity with user ID and ISBN
class Checkout:
  def __init__(self, user_id, isbn):
    self.user_id = user_id
    self.isbn = isbn

  def __repr__(self):
    return f"Checkout(user_id = {self.user_id}, isbn = {self.isbn})"

  def __eq__(self, other):
    if not isinstance(other, Checkout):
      return False
    
    return self.user_id == other.user_id and self.isbn == other.isbn
