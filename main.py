# This is a deliberately poorly implemented main script for a Library Management System.
from services.book_service import BookService
from services.user_service import UserService
from services.checkout_service import CheckoutService
from logger import log_info, log_error

book_service = BookService()
user_service = UserService()
checkout_service = CheckoutService()

def main_menu():
  print("\nLibrary Management System")
  print("1. Add Book")
  print("2. List Books")
  print("3. Update Book")
  print("4. Delete Book")
  print("5. Search Book by ISBN")
  print("6. Search Book by Title")
  print("7. Search Book by Author name")
  print("8. Add User")
  print("9. List Users")
  print("10. Update User")
  print("11. Delete User")
  print("12. Search User by ID")
  print("13. Search User by name")
  print("14. Checkout Book")
  print("15. Checkin Book")
  print("Press any key to exit (except the options)")

  choice = input("Enter choice: ")

  return choice

def main():
  while True:
    try:
      choice = main_menu()

      # Add a new book
      if choice == '1':
        title = input("Enter title: ")
        author = input("Enter author: ")
        isbn = input("Enter ISBN: ")
        is_book_added = book_service.add_book(title, author, isbn)

        if is_book_added:
          log_info("Book added.")
        else:
          log_error("Book with ISBN: {isbn} already exists")

      # List all books
      elif choice == '2':
        book_service.list_books()

      # Update an existing book
      elif choice == '3':
        isbn = input("Enter ISBN of the book to update: ")
        title = input("Enter new title (leave blank to keep current): ")
        author = input("Enter new author (leave blank to keep current): ")

        book_service.update_book(isbn, title, author)
      
      # Delete an existing book
      elif choice == '4':
        isbn = input("Enter ISBN of the book to delete: ")
        book_service.delete_book(isbn)
      
      # Search for a book (by ISBN)
      elif choice == '5':
        isbn = input("Enter ISBN to search: ")
        results = book_service.search_book_by_isbn(isbn)

        for book in results:
          print(book)

      # Search for a book (by Title)
      elif choice == '6':
        title = input("Enter title to search: ")
        results = book_service.search_book_by_title(title)

        for book in results:
          print(book)

      # Search for a book (by Author)
      elif choice == '7':
        author = input("Enter author to search: ")
        results = book_service.search_book_by_author(author)

        for book in results:
          print(book)

      # Add a new user
      elif choice == '8':
        name = input("Enter username: ")
        is_user_added = user_service.add_user(name)

        if is_user_added:
          log_info("User added.")
        else:
          log_error("User already exists")

      # List existing users
      elif choice == '9':
        user_service.list_users()

      # Update an existing user
      elif choice == '10':
        user_id = input("Enter user ID to update: ")
        name = input("Enter new name (leave blank to keep current): ")
        user_service.update_user(user_id, name)

      # Delete an existing user
      elif choice == '11':
        user_id = input("Enter user ID to delete: ")
        user_service.delete_user(user_id)

      # Search for an existing user (by ID)
      elif choice == '12':
        user_id = input("Enter user ID to search: ")
        results = user_service.search_user_by_id(user_id)

        for user in results:
          print(user)

      # Search for an existing user (by name)
      elif choice == '13':
        name = input("Enter name to search: ")
        results = user_service.search_user_by_name(name)

        for user in results:
          print(user)

      # Checkout a book
      elif choice == '14':
        user_id = input("Enter user ID: ")
        isbn = input("Enter ISBN of the book to checkout: ")
        is_checkout = checkout_service.checkout_book(user_id, isbn)

        if is_checkout:
          log_info("Book checked out.")
        else:
          log_error(f"Book ISBN: {isbn} is currently owned by User: {user_id}")

      # Checkin a book
      elif choice == '15':
        user_id = input("Enter user ID: ")
        isbn = input("Enter ISBN of the book to checkin: ")
        checkout_service.checkin_book(user_id, isbn)
        log_info("Book checked in.")

      else:
        print("Exiting.")
        break
    except Exception as e:
      log_error(f"An error occurred: {e}")

if __name__ == "__main__":
  main()
