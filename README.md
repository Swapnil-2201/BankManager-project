# BANK-MANAGER-Python Program

This repository holds a straightforward, console-based application built with **Python** to manage basic bank accounts. We used Object-Oriented Programming (OOP) to keep things clean and modular.

## 🚀 I. Project Overview & Core Features

This project simplifies the core functions of a basic bank. You can set up new accounts, log in securely, and handle your deposits and withdrawals right from your terminal.

### What's Inside:

* **Clean OOP Structure:** The application uses two main components, `BankAcc` and `userManager`, to cleanly separate banking logic from account management.
* **Unique Accounts:** Easily create new user accounts; each one gets its own unique, 10-digit account number.
* **Simple Authentication:** Implements a basic login system using a user ID and password.
* **Transaction Logic:** Includes robust methods for **depositing** and **withdrawing** funds, with built-in checks to prevent negative amounts and insufficient funds.
* **Interest Rate:** A class-level interest rate can be applied to balances.
* **Menu-Driven Interface:** The application is easy to use thanks to a structured command-line menu that guides the user through all available actions.

## 🛠️ II. Technical Setup

* **Language:** Python 3.x or a newer version.
* **Dependencies:** None—just a standard Python compiler.

## ▶️ III. Execution Instructions

1.  **File Naming:** Ensure the Python source code file is saved as **`Bankmanager.py`**.
2.  **Run the System:** Navigate to the file's directory in your terminal and run the following command:

    ```bash
    python Bankmanager.py
    ```

## 💻 IV. How to Use the System

The system starts by immediately displaying the Main Login/Creation Menu. It automatically sets up a few accounts for testing purposes.

* **Pre-set Test Accounts:**
    * ID: `Harsh Singh`, Password: `123`
    * ID: `Shraddha Kapoor`, Password: `pass`
* **Main Menu Options:** From the main screen, you can **Log In** to an existing account, **Create New Account** (after accepting the T&C), or **Exit System**.
* **Account Actions:** Once logged in, you can check your balance, and initiate deposits and withdrawals.

## ✅ V. Required Testing & Validation

To ensure everything works correctly, please perform these tests and capture a screenshot for each required step.

| Test Case | Steps to Perform | Expected Outcome | Screenshot Required |
| :--- | :--- | :--- | :--- |
| **T1: Account Creation** | 1. Select **2 (Create New Account)**. 2. Accept T&C. 3. Enter credentials and an initial deposit (e.g., $1000). | Confirmed creation message showing the new user ID and the unique 10-digit Account Number. | **Yes** (Proof of successful creation) |
| **T2: Successful Login** | 1. Select **1 (Log In)**. 2. Use a predefined account (e.g., ID: `Harsh Singh`, Pass: `123`). | The system confirms login and immediately shows the **User Actions Menu** and **Account Statistics**. | **Yes** (Proof of accessing the account menu) |
| **T3: Funds Deposit** | 1. Log in (T2). 2. Select **1 (Deposit)**. 3. Enter a positive amount (e.g., 500.00). | System confirms the deposit; the **Current Balance** in the statistics updates correctly. | **Yes** (Proof of updated balance) |
| **T4: Successful Withdrawal** | 1. Stay logged in (T3). 2. Select **2 (Withdraw)**. 3. Enter an amount **lower than** the current balance. | System confirms "Withdrawal successful," and the **Current Balance** is reduced. | **Yes** (Proof of reduced balance) |
| **T5: Insufficient Funds Check** | 1. Stay logged in (T4). 2. Select **2 (Withdraw)**. 3. Enter an amount **higher than** the current balance. | The error message "Insufficient funds! Withdrawal cancelled." appears. | **Yes** (Proof of the error message) |
| **T6: Logout and Exit** | 1. Logged in: Select **3 (Log Out)**. 2. Main Menu: Select **4 (Exit System)**. | Session ends, returning to the Main Menu, and the program terminates cleanly. | **No** |

## 📂 VI. Repository Contents

* **`Bankmanager.py`**: The core Python code with all class definitions (`BankAcc`, `userManager`) and execution logic.
* **`README.md`**: This file, serving as the main project documentation, instructions, and feature guide.
* **`statement.md`**: Detailed design document outlining the OOP architecture and key structural decisions.

<img width="1062" height="748" alt="image" src="https://github.com/user-attachments/assets/bbe0f5c3-07f4-48a6-a0c7-8e00c97b0174" />

<img width="736" height="839" alt="image" src="https://github.com/user-attachments/assets/c39b9218-1fc7-4884-9535-e7fce13133f1" />


