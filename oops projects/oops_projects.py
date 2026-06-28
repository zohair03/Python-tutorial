from bank_account import *

zohair = BankAccount(5000,"Zohair")
ahmed = BankAccount(2000,"Ahmed")
sheikh = InterestRewardsAcct(0,"Sheikh")

zohair.get_balance()
ahmed.get_balance()
sheikh.get_balance()

zohair.deposit(500)
ahmed.deposit(421)
sheikh.deposit(100)

zohair.withdraw(500)
ahmed.withdraw(2000)

zohair.transfer_funds(ahmed,1000)