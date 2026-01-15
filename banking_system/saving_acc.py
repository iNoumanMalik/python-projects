from account import Account
from transaction import Transaction
from exception import (InvalidAmountError, InsufficientBalanceError)


class SavingAccount(Account):
    MIN_BALANCE = 500
    
    def withdraw(self, amount, record_tx=True):
        if amount<=0:
            raise InvalidAmountError("Withdraw amount must be positive")
        
        if self.balance - amount < self.MIN_BALANCE:
            raise InsufficientBalanceError(f"You should have at least {self.MIN_BALANCE} for a transaction")
        
        self.balance -= amount
        
        if record_tx:
            self._add_transaction(amount,"withdraw")