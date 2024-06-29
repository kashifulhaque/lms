import unittest

from services.book_service import BookService
from services.user_service import UserService
from services.checkout_service import CheckoutService

class TestCalculations(unittest.TestCase):
  title = "CUDA by Example: An Introduction to General-Purpose GPU Programming"
  author = " Jason Sanders, Edward Kandrot"
  isbn = "0131387685"

  user_id = "1"
  username = "kashifulhaque"

  book_service = BookService()
  user_service = UserService()
  checkout_service = CheckoutService()

  def test_add_book(self):
    is_book_added = self.book_service.add_book(
      self.title,
      self.author,
      self.isbn
    )
    self.assertEqual(is_book_added, True, "Failed to add book")
  
  def test_search_book_isbn(self):
    search_result = self.book_service.search_book_by_isbn(self.isbn)
    self.assertEqual(len(search_result), 1, f"No such book with ISBN: {self.isbn}")
  
  def test_search_book_title(self):
    search_result = self.book_service.search_book_by_title(self.title)
    self.assertEqual(len(search_result), 1, f"No such book with title: {self.title}")
  
  def test_search_book_author(self):
    search_result = self.book_service.search_book_by_author(self.author)
    self.assertEqual(len(search_result), 1, f"No such book with author name: {self.author}")
  
  def test_add_user(self):
    is_user_added = self.user_service.add_user(self.username)
    self.assertEqual(is_user_added, True, "Failed to add user")

  def test_search_user_id(self):
    search_results = self.user_service.search_user_by_id(self.user_id)
    self.assertEqual(len(search_results), 1, f"No user found with ID: {self.user_id}")

  def test_search_user_name(self):
    search_results = self.user_service.search_user_by_name(self.username)
    self.assertEqual(len(search_results), 1, f"No user found with username: {self.username}")

  def test_book_checkout_true(self):
    is_checkout = self.checkout_service.checkout_book(self.user_id, self.isbn)
    self.assertEqual(is_checkout, True, "Failed to checkout book")
  
  def test_book_available(self):
    is_available = self.checkout_service.check_book_availability(self.isbn)
    self.assertEqual(is_available, True, f"Book {self.isbn} is not available")

if __name__ == "__main__":
  unittest.main()