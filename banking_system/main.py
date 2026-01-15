from bank import Bank

bank = Bank()

saving_acc_id = bank.create_account("saving",2000)
current_acc_id = bank.create_account("current",2000)

savings = bank.get_account(saving_acc_id)
current = bank.get_account(current_acc_id)

savings.deposit(1000)
current.deposit(5000)

print("Saving Balance: ", savings.get_balance())
print("Current Balance:", current.get_balance())

savings.withdraw(200,)
current.withdraw(100,)

print("Saving Balance: ", savings.get_balance())
print("Current Balance:", current.get_balance())

bank.transfer(saving_acc_id,current_acc_id,400)

print("\nSavings Transactions:")
savings.show_transactions()

print("\nCurrent Transactions:")
current.show_transactions()
