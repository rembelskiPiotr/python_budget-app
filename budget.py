class Category:
  
  def __init__(self, input_name):
    self.category_name = input_name
    self.ledger = []
    self.balance = 0
    self.expenses = 0
    self.percent = 0

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})
    self.balance += amount

  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      self.balance -= amount
      self.expenses += amount
      return True
    else:
      return False

  def get_balance(self):
    return self.balance

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

  def calculate_percentage(self, all_expenses):
    self.percent = round_to_ten(self.expenses / all_expenses * 100)  
    
  def __str__(self):
    printout = self.category_name.center(30,"*") + "\n"
    for entry in self.ledger:
      printout += entry["description"][:23].ljust(23)
      printout += str("{:.2f}".format(entry["amount"]).rjust(7)) + "\n"
    printout += "Total: " + str(self.get_balance())
    return printout

def create_spend_chart(categories):
  all_expenses = get_all_expenses(categories)
 
  bar_chart = "Percentage spent by category" + "\n"
  axis_label = 100

  while axis_label >= 0:
    bar_chart += str(axis_label).rjust(3) + "|" + " "

    for category in categories:
      category.calculate_percentage(all_expenses)
      if category.percent >= axis_label:
        bar_chart += "o" + 2 * " "
      else:
        bar_chart += 3 * " "
    axis_label -= 10 
    bar_chart += "\n"

  bar_chart += 4 * " " + ("-" * (1 + 3 * len(categories))) + "\n"
  longest_category_name = get_longest_category_name(categories)
  
  for row in range(longest_category_name):
    bar_chart += 5 * " "
    for category in categories:
      if len(category.category_name) - 1 < row:
        bar_chart += 3 * " "
      else:
        bar_chart += category.category_name[row] + 2 * " "
    if row != longest_category_name - 1:  
      bar_chart += "\n"
  return bar_chart

def get_all_expenses(categories):
  all_expenses = 0
  for category in categories:
    all_expenses += category.expenses
  return all_expenses
  
def round_to_ten(number):
  if number < 10:
    return 0
  return round(number / 10) * 10

def get_longest_category_name(categories):
  longest_category_name = 0
  for category in categories:
    if len(category.category_name) > longest_category_name:
      longest_category_name = len(category.category_name)
  return longest_category_name