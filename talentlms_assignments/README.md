# 🐍 Python Assignments – TalentLMS

This repository contains my **Python assignments** completed as part of the **TalentLMS Python course**. The assignments are divided into three levels: **Easy**, **Medium**, and **Hard**, covering fundamental to intermediate Python concepts.

---

## 📁 Repository Structure

```
python-assignments/
│
├── easy/
│   ├── calculator.py
│   ├── temperature_converter.py
│   ├── vowel_counter.py
│   └── list_operations.py
│
├── medium/
│   ├── fibonacci.py
│   ├── word_frequency.py
│   ├── data_validation.py
│   └── file_handling/
│       ├── students.csv
│       ├── average_grades.py
│       └── address_book.py
│
├── hard/
│   └── hangman.py
│
└── README.md
```

---

## ✅ Assignment: Easy

### 1️⃣ Calculator

A function that takes two numbers and an operator (`+`, `-`, `*`, `/`) and returns the calculated result.

**Example:**

```
Input: 5, 3, "*"
Output: 15
```

---

### 2️⃣ Temperature Converter

Converts temperature between **Celsius** and **Fahrenheit**.

**Example:**

```
Input: 25 Celsius
Output: 77.0 Fahrenheit
```

---

### 3️⃣ Vowel Counter

Counts the number of vowels (`a, e, i, o, u`) in a given string.

**Example:**

```
Input: "Hello, world!"
Output: 3
```

---

### 4️⃣ List Operations

Functions to:

* Calculate **sum**, **average**, and **maximum** of a list
* Reverse a list

**Example:**

```
Input: [1, 5, 3, 8, 2]
Sum: 19
Average: 3.8
Maximum: 8
```

```
Input: ['a', 'b', 'c']
Output: ['c', 'b', 'a']
```

---

## 🟡 Assignment: Medium

### 1️⃣ Fibonacci Sequence

Generates the first `n` numbers of the Fibonacci sequence.

**Example:**

```
Input: 8
Output: [0, 1, 1, 2, 3, 5, 8, 13]
```

---

### 2️⃣ Word Frequency Counter

Reads a text file and counts how many times each word appears.

**Example:**

```
Input Text: "This is a test. This is only a test."
Output: {'This': 2, 'is': 2, 'a': 2, 'test': 2, 'only': 1}
```

---

### 3️⃣ Data Validation

Validates user input for:

* Integer
* Float
* Email address

**Example:**

```
Input: "5", "integer"
Output: True

Input: "example@email.com", "email"
Output: True
```

---

### 4️⃣ File Handling

#### 📌 Student Average Calculator

Reads a CSV file containing student names and grades, then prints the **average grade** for each student.

#### 📌 Text-Based Address Book

Allows the user to:

* Add a contact (name & phone number)
* Search for a contact by name

Data is stored persistently in a text file.

---

## 🔴 Assignment: Hard

### 🎯 Hangman Game

A console-based Hangman game with the following features:

* Random secret word selection
* Display of blanks (`_`) for unguessed letters
* User letter input
* Tracking of correct and incorrect guesses
* Visual representation of incorrect guesses
* Win condition: all letters guessed correctly
* Lose condition: maximum incorrect guesses reached

---

## 🚀 How to Run the Programs

1. Clone the repository:

```bash
git clone <repository-link>
```

2. Navigate to the assignment folder:

```bash
cd python-assignments
```

3. Run any Python file:

```bash
python filename.py
```

---

## 🛠 Technologies Used

* Python 3
* File Handling
* Functions
* Loops & Conditionals
* Lists, Dictionaries, Strings

---

## 📌 Notes

* All assignments are written without Object-Oriented Programming (where not required).
* Focus is on **logic building**, **file handling**, and **core Python concepts**.
* This repository is submitted as part of the **TalentLMS Python course**.

---

## 👤 Author

**Nouman**

---

✅ *End of README*
