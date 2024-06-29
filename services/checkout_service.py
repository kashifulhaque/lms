from models.checkout import Checkout
from storage import Storage

class CheckoutService:
  _instance = None

  def __new__(cls, *args, **kwargs):
    if not cls._instance:
      cls._instance = super(CheckoutService, cls).__new__(cls, *args, **kwargs)

    return cls._instance

  def __init__(self):
    self.storage = Storage('checkouts.csv')
    self.checkouts = self.storage.load()

  def checkout_book(self, user_id, isbn):
    checkout = Checkout(user_id, isbn)
    self.checkouts.append(checkout)
    self.storage.save(self.checkouts)

  def checkin_book(self, user_id, isbn):
    self.checkouts = [checkout for checkout in self.checkouts if not (checkout.user_id == user_id and checkout.isbn == isbn)]
    self.storage.save(self.checkouts)
