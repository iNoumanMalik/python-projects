from exception import (InsufficientBalanceError,InvalidAmountError)
from abc import ABC, abstractmethod
from transaction import Transaction

class Account(ABC):
    _account_counter = 1000
    def __init__(self,initial_balance):
        if(initial_balance<0):
            raise InvalidAmountError("Deposit amount must be positive")
        
        Account._account_counter+=1
        self.account_number += Account._account_counter
        self.balance = initial_balance
        self.transactions = []
    
    def deposit(self,amount):
        if(amount<=0):
            raise InvalidAmountError("Deposit amount must be positive")
        
        self.balance +=amount
        self._add_transaction(amount,"deposit")
        
    @abstractmethod
    def withdraw(self,amount):
        pass
        
    def _add_transaction(self,amount,tx_type,desc=""):
        tx_history = Transaction(amount,tx_type,desc)
        self.transactions.append(tx_history)
    
    def get_balance(self):
        if(self.balance<=0):
            raise InsufficientBalanceError
        return self.balance
    
    def show_transactions(self):
        for tx in self.transactions:
            print(tx)
    
    