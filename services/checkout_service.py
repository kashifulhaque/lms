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

    for ele in self.checkouts:
      if ele == checkout:
        return False

    self.checkouts.append(checkout)
    self.storage.save(self.checkouts)
    self.__init__()
    return True

  def checkin_book(self, user_id, isbn):
    checkin = Checkout(user_id, isbn)
    results = []

    for checkout in self.checkouts:
      if checkout == checkin:
        pass
      else:
        results.append(checkout)

    self.checkouts = results
    self.storage.save(self.checkouts)
    self.__init__()
