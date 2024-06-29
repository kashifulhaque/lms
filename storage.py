import csv
import os
from models.book import Book
from models.user import User
from models.checkout import Checkout

# Storage class handles saving and loading data from CSV files
class Storage:
  def __init__(self, filename):
    self.filename = filename

  def save(self, data):
    if not data:
      return

    # Check the type of data and call the respective save method
    if isinstance(data[0], Book):
      self._save_books(data)
    elif isinstance(data[0], User):
      self._save_users(data)
    elif isinstance(data[0], Checkout):
      self._save_checkouts(data)

  def load(self):
    if not os.path.exists(self.filename):
      return []

    # Load data from the CSV file
    with open(self.filename, "r", newline = "") as file:
      reader = csv.reader(file)
      data = [self._dict_to_object(row) for row in reader]

    return data

  # Private methods to save data for each model
  def _save_books(self, books):
    with open(self.filename, "w", newline = "") as file:
      writer = csv.writer(file)

      for book in books:
        writer.writerow([book.title, book.author, book.isbn])

  def _save_users(self, users):
    with open(self.filename, "w", newline = "") as file:
      writer = csv.writer(file)

      for user in users:
        writer.writerow([user.name, user.user_id])

  def _save_checkouts(self, checkouts):
    with open(self.filename, "w", newline = "") as file:
      writer = csv.writer(file)

      for checkout in checkouts:
        writer.writerow([checkout.user_id, checkout.isbn])

  # Convert CSV row data back to respective model objects
  def _dict_to_object(self, row):
    if self.filename == "books.csv":
      return Book(row[0], row[1], row[2])
    elif self.filename == "users.csv":
      return User(row[0], row[1])
    elif self.filename == "checkouts.csv":
      return Checkout(row[0], row[1])
