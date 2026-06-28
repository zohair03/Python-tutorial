class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, intialBalance, accName):
        self.balance = intialBalance
        self.name = accName
        print(f"Account '{self.name}' has created\nBalance: ${self.balance}\n")
    
    def get_balance(self):
        print(f"Account '{self.name}' balance:${self.balance:.2f}\n")

    def deposit(self,ammount):
        self.balance = self.balance + ammount
        print(f"Deposit of '{ammount}' is Completed!!")
        self.get_balance()

    def viableTransactions(self, ammount):
        if self.balance >= ammount:
            return
        else:
            raise BalanceException(f"Account '{self.name}' has only balance of ${self.balance}")
    
    def withdraw(self, ammount):
        try:
            self.viableTransactions(ammount)
            self.balance = self.balance - ammount
            print(f"${ammount} has been withdrawn from '{self.name}'")
            self.get_balance()
        except Exception as error:
            print(f"\nError in withdrawing money : {error}")
    
    def transfer_funds(self, account, ammount):
        try:
            self.viableTransactions(ammount)
            self.balance = self.balance - ammount
            account.balance = account.balance + ammount
            print(f"Transfer of ${ammount} is Susseccfull!!")
            self.get_balance()
            account.get_balance()
        except Exception as error:
            print(f"\nError in transfering funds: {error}")


class InterestRewardsAcct(BankAccount): 
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit complete.")
        self.get_balance()