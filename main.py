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
  print("5. Search Books")
  print("6. Add User")
  print("7. List Users")
  print("8. Update User")
  print("9. Delete User")
  print("10. Search Users")
  print("11. Checkout Book")
  print("12. Checkin Book")
  print("13. Exit")

  choice = input("Enter choice: ")

  return choice

def main():
  while True:
    try:
      choice = main_menu()

      if choice == '1':
        title = input("Enter title: ")
        author = input("Enter author: ")
        isbn = input("Enter ISBN: ")
        is_book_added = book_service.add_book(title, author, isbn)

        if is_book_added:
          log_info("Book added.")
        else:
          log_error("Book with ISBN: {isbn} already exists")

      elif choice == '2':
        book_service.list_books()

      elif choice == '3':
        isbn = input("Enter ISBN of the book to update: ")
        title = input("Enter new title (leave blank to keep current): ")
        author = input("Enter new author (leave blank to keep current): ")

        book_service.update_book(isbn, title, author)
      
      elif choice == '4':
        isbn = input("Enter ISBN of the book to delete: ")
        book_service.delete_book(isbn)
      
      elif choice == '5':
        isbn = input("Enter ISBN to search: ")
        results = book_service.search_books(isbn)

        for book in results:
          print(book)
      
      elif choice == '6':
        name = input("Enter user name: ")
        user_id = input("Enter user ID: ")
        user_service.add_user(name, user_id)
        log_info("User added.")

      elif choice == '7':
        user_service.list_users()

      elif choice == '8':
        user_id = input("Enter user ID of the user to update: ")
        name = input("Enter new name (leave blank to keep current): ")
        user_service.update_user(user_id, name)

      elif choice == '9':
        user_id = input("Enter user ID of the user to delete: ")
        user_service.delete_user(user_id)

      elif choice == '10':
        name = input("Enter name to search: ")
        user_id = input("Enter user ID to search: ")
        results = user_service.search_users(name, user_id)

        for user in results:
          print(user)

      elif choice == '11':
        user_id = input("Enter user ID: ")
        isbn = input("Enter ISBN of the book to checkout: ")
        checkout_service.checkout_book(user_id, isbn)
        log_info("Book checked out.")

      elif choice == '12':
        user_id = input("Enter user ID: ")
        isbn = input("Enter ISBN of the book to checkin: ")
        checkout_service.checkin_book(user_id, isbn)
        log_info("Book checked in.")

      elif choice == '13':
        print("Exiting.")
        break

      else:
        print("Invalid choice, please try again.")
    except Exception as e:
      log_error(f"An error occurred: {e}")

if __name__ == "__main__":
  main()
