from models.user import User
from storage import Storage

from thefuzz import fuzz

# UserService class handles operations related to users
class UserService:
  _instance = None

  def __new__(cls, *args, **kwargs):
    if not cls._instance:
      cls._instance = super(UserService, cls).__new__(cls, *args, **kwargs)

    return cls._instance

  def __init__(self):
    self.storage = Storage('users.csv')
    self.users = self.storage.load()

  # Add a new user
  def add_user(self, name):
    user_id = len(self.users) + 1
    user = User(name, user_id)

    for ele in self.users:
      if ele == user:
        return False
    
    self.users.append(user)
    self.storage.save(self.users)
    self.__init__()
    return True

  # List all users
  def list_users(self):
    print(f"| User ID\t| Username\t|")
    for user in self.users:
      print(f"| {user.user_id}\t\t| {user.name}\t|")

  # Update user details
  def update_user(self, user_id, name = None):
    for user in self.users:
      if user.user_id == user_id:
        if name:
          user.name = name

        self.storage.save(self.users)
        self.__init__()
        return
      
    print("User not found.")

  # Delete a user
  def delete_user(self, user_id):
    self.users = [user for user in self.users if user.user_id != user_id]
    self.storage.save(self.users)
    self.__init__()

  # Search a yser by ID
  def search_user_by_id(self, user_id):
    results = []

    for user in self.users:
      if user_id and user_id == user.user_id:
        results.append(user)

    return results

  # Search a user by name
  def search_user_by_name(self, name):
    results = []

    for user in self.users:
      ratio = fuzz.token_set_ratio(name, user.name)
      
      if name and ratio >= 50:
        results.append(user)

    return results
