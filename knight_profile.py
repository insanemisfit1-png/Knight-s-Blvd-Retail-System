
product = "Black Hoodie"
size = "Medium"
price = "799.99"
color = "Black"
style = "Streetwear"
age = 22
name = "Bhlomingtn"


name = input("What's your name?")
print("Welcome,", name)

product = input("what product are you looking for?")
size = input("what size do you need?") 


budget = 600
if budget >= 800:
      print("Premium Hoodie")
else:
      print("Standard Hoodie") 


      budget = 1200

      if budget >= 1200:
        print("Luxury Collection")
      elif budget>= 800:
          print("Premium Collection")
      else:
          print("Essential Collection")

        




budget = int( input("what's your budget?"))
print("Welcome,", name)

if budget>= 1200:
        print("We recommennd our Luxury Collection.")
elif budget>= 800:
          print("We recommend our Premium Collection.")
else:
          print("We recommend our Essential Collection.")


# Abstract budget class and a concrete implementation
from abc import ABC, abstractmethod


class budget(ABC):
  """Abstract budget interface."""

  @abstractmethod
  def set_budget(self, amount: float):
    pass

  @abstractmethod
  def get_budget(self) -> float:
    pass

  @abstractmethod
  def recommend_collection(self) -> str:
    pass

  @abstractmethod
  def apply_discount(self, price: float) -> float:
    pass


class BudgetImpl(budget):
  """Concrete implementation of budget logic."""

  def __init__(self, amount: float = 0.0):
    self._budget = float(amount)

  def set_budget(self, amount: float):
    self._budget = float(amount)

  def get_budget(self) -> float:
    return self._budget

  def recommend_collection(self) -> str:
    if self._budget >= 1200:
      return "Luxury Collection"
    if self._budget >= 800:
      return "Premium Collection"
    return "Essential Collection"

  def apply_discount(self, price: float) -> float:
    """Apply a simple discount based on budget tiers.

    - Luxury: 20% off
    - Premium: 10% off
    - Essential: 0% off
    """
    if price is None:
      return 0.0
    p = float(price)
    if self._budget >= 1200:
      return round(p * 0.80, 2)
    if self._budget >= 800:
      return round(p * 0.90, 2)
    return round(p, 2)


# Example usage (non-intrusive): create an instance if budget variable exists
try:
  _b = BudgetImpl(budget)
except Exception:
  _b = BudgetImpl(0)















