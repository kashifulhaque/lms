class Checkout:
  def __init__(self, user_id, isbn):
    self.user_id = user_id
    self.isbn = isbn

  def __repr__(self):
    return f"Checkout(user_id = {self.user_id}, isbn = {self.isbn})"
