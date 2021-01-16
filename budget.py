class Category:
  category_name = ""

  def __init__(self, input_name):
    self.category_name = input_name
    self.ledger = []

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.deposit(-amount, description)
      return True
    else:
      return False

  def get_balance(self):
    return sum_by_key(self.ledger, "amount")

  def transfer(self, amount, budget_category):
    if self.check_funds(amount):
      self.withdraw(amount,"Transfer to " + budget_category.category_name)
      budget_category.deposit(amount, "Transfer from " + self.category_name)
      return True
    else:
      return False
    
  def check_funds(self, amount):
    if amount > self.get_balance():
      return False
    else:
      return True
  
  def __str__(self):
    printout = self.category_name.center(30,"*") + "\n"
    for element in self.ledger:
      printout += element["description"][:23].ljust(23)
      printout += str("{:.2f}".format(element["amount"]).rjust(7)) + "\n"
    printout += "Total: " + str(self.get_balance())
    return printout



def create_spend_chart(categories):
  

def sum_by_key(list, key):
  result = 0
  for element in list:
    result += element[key]
  return result
  