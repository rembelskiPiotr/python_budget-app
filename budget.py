class Category:
  ledger = []
  name = ""

  def __init__(self, input_name):
    self.name = input_name

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})
  def 



def create_spend_chart(categories):