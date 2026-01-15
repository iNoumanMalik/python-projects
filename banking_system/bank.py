from saving_acc import SavingAccount
from currect_acc import CurrentAccount
from exception import (InsufficientBalanceError,InvalidAmountError,AccountNotFoundError)

class Bank:
    def __init__(self):
        self.accounts = {}
        
    def create_account(self,acc_type,initial_balance):
        if(acc_type=="saving"):
            acc = SavingAccount(initial_balance)
        elif(acc_type=="current"):
            acc = CurrentAccount(initial_balance)
        else:
            raise ValueError("Invalid Account Type")
        
        self.accounts[acc.account_number] = acc
        return acc.account_number
        
        
        
    def get_account(self,account_number):
        account = self.accounts.get(account_number)
        if not account:
            raise AccountNotFoundError("Account not found")
        return account 
            
    def transfer(self,from_acc_no,to_acc_no,amount):
        if amount<0:
            raise InvalidAmountError("Withdraw amount must be positive")
        
        from_acc = self.get_account(from_acc_no)
        to_acc = self.get_account(to_acc_no)
        
        from_acc.withdraw(amount, record_tx=False)
        to_acc.deposit(amount, record_tx=False)
        
        from_acc._add_transaction(amount, "transfer", f"To {to_acc_no}")
        to_acc._add_transaction(amount, "transfer", f"From {from_acc_no}")
        
        
        
        