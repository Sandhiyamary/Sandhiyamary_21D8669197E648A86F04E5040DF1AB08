class Bankaccount:

  def __init__(self, account_number, account_holder_name, initial_balance = 0.0):
    self.__account_number = account_number 
    self.__account_holder_name = account_holder_name 
    self.__account_balance = initial_balance 

  def deposit (self, amount):
    if amount > 0:
      self.__account_balance += amount 
      #self.__account_balance = self.__account_balance-amount
      print("deposit ₹{}.new balance: ₹{}".format(amount,self.__amount_balance))
   
    else:
      print("Invaild deposit amount.please deposit positive amount.")

  def withdraw (self,amount):
    if amount > 0 and amount <= self.__account_balance:
      self.__account_balance -= amount 
      #self.__account_balance = self.__account_balance-amount
      print("withdraw ₹{}. new balance: ₹{}".format(amount,self.__account_balance))

    else:
      print ("invaild withdrawal amount.please withdraw a positive amount.")

  def display_balance (self):
     print("account balance for{}(account{}):.₹{}".format(self.__amount_holder_name,self.__amount_number,self.__amount_balance))
    account=Bankaccount(account_number="123456",               account_holder_name="sandy",
              initial_balance=5000.0)
     account. display_balance ()
     account. deposit(500.0)
     account. withdraw (200.0)
     account. display_balance ()