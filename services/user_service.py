from models.user import User
from storage import Storage

class UserService:
  _instance = None

  def __new__(cls, *args, **kwargs):
    if not cls._instance:
      cls._instance = super(UserService, cls).__new__(cls, *args, **kwargs)

    return cls._instance

  def __init__(self):
    self.storage = Storage('users.csv')
    self.users = self.storage.load()

  def add_user(self, name):
    user_id = len(self.users) + 1
    user = User(name, user_id)

    for ele in self.users:
      if ele == user:
        return False
    
    self.users.append(user)
    self.storage.save(self.users)
    return True

  def list_users(self):
    for user in self.users:
      print(user)

  def update_user(self, user_id, name = None):
    for user in self.users:
      if user.user_id == user_id:
        if name:
          user.name = name

        self.storage.save(self.users)
        return
      
    print("User not found.")

  def delete_user(self, user_id):
    for u in self.users:
      print(u)
  
    self.users = [user for user in self.users if user.user_id != user_id]
    self.storage.save(self.users)

  def search_users(self, name = None, user_id = None):
    results = []

    for user in self.users:
      if name and name in user.name:
        results.append(user)

      if user_id and user_id == user.user_id:
        results.append(user)

    return results
