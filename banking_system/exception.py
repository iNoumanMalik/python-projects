class BankingError(Exception):
    pass

class InvalidAmountError(BankingError):
    pass

class InsufficientBalanceError(BankingError):
    pass

class AccountNotFoundError(BankingError):
    pass

