from account import Account
from exception import (InvalidAmountError, InsufficientBalanceError)


class CurrentAccount(Account):
    OVERDRAFT_LIMIT = 1000
    
    def withdraw(self, amount,record_tx=True):
        if amount<0:
            raise InvalidAmountError("Withdraw amount must be positive")
        
        if self.balance - amount < -self.OVERDRAFT_LIMIT:
            raise InsufficientBalanceError("Overdraft limit exceeds")
            
        self.balance -= amount
        
        if record_tx:
            self._add_transaction(amount,"withdraw")