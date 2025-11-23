# BankManager-project

This repository contains a foundational console-based application designed for basic bank account management, developed using Python and Object-Oriented Programming (OOP) principles.

## I. Project Overview and Features

The system facilitates the core operations required for a simple banking environment, including user account creation, secure login, and financial transaction processing.

### Key Features:

* **Object-Oriented Design:** The architecture utilizes dedicated `BankAccount` and `UserManager` classes to ensure modularity and separation of concerns.
* **Account Administration:** Supports the creation of new user accounts, each assigned a unique 10-digit account identifier.
* **User Authentication:** Implements basic login functionality with user ID and password verification.
* **Transaction Processing:** Features robust methods for `deposit` and `withdraw` operations, including validation checks for positive amounts and sufficient account funds.
* **Financial Logic:** Incorporates a class-level interest rate mechanism that can be applied to account balances.
* **Interface:** A structured, menu-driven command-line interface guides the user through available operations.

## II. Technical Requirements

* **Programming Language:** Python 3.x or higher
* **Compiler:** Any python compiler

## III. Execution Guide

1.  **File Setup:** Save the provided Python source code as `Bankmanager.py`.
2.  **System Execution:** Navigate to the file's directory within your terminal or command prompt and execute the following command:

    ```bash
    python Bankmanager.py
    ```

## IV. System Usage

Upon launch, the system initializes several accounts for testing purposes and presents the Main Login/Creation Menu.

* **Initial Test Accounts:**
    * ID: `Harsh Singh`, Password: `123`
    * ID: `Shraddha kapoor`, Password: `pass`
* **Main Operations:** Users can choose to **Log In** to an existing account, **Create New Account** after reviewing the Terms & Conditions, or **Exit System**.
* **Account Operations:** Once authenticated, users can view their balance, perform deposits, and execute withdrawals.

## V. Testing Instructions and Required Screenshots

To verify the correct functionality of the system, please perform the following tests. A screenshot must be captured after the successful completion of each test case.

| Test Case | Steps to Perform | Expected Outcome | Screenshot Required |
| :--- | :--- | :--- | :--- |
| **T1: Account Creation** | 1. Choose option **2 (Create New Account)**. 2. Accept T&C. 3. Enter a new ID, Password, and Initial Deposit (e.g., $1000). | System confirms the new user is created and displays the new 10-digit Account Number. | **Yes** (Showing successful creation) |
| **T2: Successful Login** | 1. Choose option **1 (Log In)**. 2. Use a predefined account (e.g., ID: `Harsh Singh`, Pass: `123`). | Login successful message, followed by the **User Actions Menu** and **Account Statistics**. | **Yes** (Showing logged-in menu) |
| **T3: Funds Deposit** | 1. Log in to an account (T2). 2. Select option **1 (Deposit)**. 3. Enter a positive amount (e.g., 500.00). | System confirms successful deposit, and the **Current Balance** in the Account Statistics is updated. | **Yes** (Showing updated balance) |
| **T4: Successful Withdrawal** | 1. Stay logged in (T3). 2. Select option **2 (Withdraw)**. 3. Enter an amount **less than** the current balance. | System confirms "Withdrawal successful," and the **Current Balance** is reduced accordingly. | **Yes** (Showing reduced balance) |
| **T5: Insufficient Funds Check** | 1. Stay logged in (T4). 2. Select option **2 (Withdraw)**. 3. Enter an amount **greater than** the current balance. | System prints the error message: "Insufficient funds! Withdrawal cancelled." | **Yes** (Showing the error message) |
| **T6: Logout and Exit** | 1. Logged in: Select option **3 (Log Out)**. 2. Main Menu: Select option **4 (Exit System)**. | The session returns to the Main Menu, and then the system shuts down, respectively. | **No** (Verification of system closure is sufficient) |

## VI. Repository Structure

* **Bankmanager.py**: The primary Python source code file containing all class definitions (BankAccount, UserManager) and the main program logic.
* **README.md**: The main documentation file, providing an overview of the project, features, and instructions for setup and running the system.
* **statement.md**: The design and architectural statement detailing the OOP structure, class responsibilities, and key design decisions.

<img width="1020" height="968" alt="image" src="https://github.com/user-attachments/assets/e9cf6d48-4e2b-4438-b4b5-c9175b0c7a98" />
<img width="828" height="804" alt="image" src="https://github.com/user-attachments/assets/cb0c1931-0fee-48f3-9d0d-f6b0cd02053d" />

