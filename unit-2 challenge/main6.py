class bankaccount:
  def __init__(self,account_number,account_holdername,initial_balance=0.0):
    self.__account_number=account_number
    self.__account_holdername=account_holdername
    self.__account_balance=initial_balance
  def deposit(self,amount):
    if amount>0 :
      self.__account_balance+=amount
      print("deposited {}.new balance:{}".format(amount,self.__account_balance))
    else:
      print("invalid deposit amount.please enter positive  number")
  def withdraw(self,amount):
    if amount>0 and amount<=self.__account_balance:
      self.__account_balance-= amount
      print("withdraw {} .new balance {}".format(amount,self.__account_balance))
    else:
      print("invalid withdrawl amount please enter valid withdraw amount.")
  def display_balance(self):
    print("account balance for{}(account#{}):{}".format(self.__account_holdername,self.__account_balance,self.__account_balance))
account=bankaccount(account_number="9893374893",account_holdername="vishal",initial_balance=6000.0)
account.display_balance()
account.deposit(500.0)
account.withdraw(200.0)
account.display_balance()