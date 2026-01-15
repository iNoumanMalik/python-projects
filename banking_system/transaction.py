from datetime import datetime

class Transaction:
    def __init__(self,amount,tx_type, description):
        self.amount = amount
        self.tx_type = tx_type
        self.description = description
        self.timestamp = datetime.now()
    
    # __rept__ is like __str__ , it is developer friendly string representation of an object
    def __repr__(self):
        return f"{self.amount} {self.tx_type} {self.description} {self.timestamp}"