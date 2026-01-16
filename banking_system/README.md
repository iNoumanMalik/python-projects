# 🏦 Python Banking System

A simple **console-based banking system** built using **Python and OOP principles**.  
This project focuses on clean architecture, business rules, and backend-style design.

---

## 📌 Features

- Create Savings and Current accounts
- Deposit, withdraw, and transfer money
- Account-specific balance rules
- Transaction history tracking
- Custom exception handling
- Input validation and error safety

---

## 🧠 Concepts Used

- Object-Oriented Programming (OOP)
- Abstract Base Classes (`abc`)
- Method overriding
- Encapsulation
- Composition (Account → Transactions)
- Custom Exceptions
- Service-layer design (Bank as coordinator)

---

## 🗂️ Project Structure

banking_system/
│
├── main.py # Entry point
├── bank.py # Bank service (account management & transfers)
├── account.py # Abstract Account class
├── savings_acc.py # Savings account logic
├── current_acc.py # Current account logic
├── transaction.py # Transaction model
└── exception.py # Custom exceptions


---

## ▶️ How to Run

```bash
python main.py
