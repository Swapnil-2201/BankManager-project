# BankManager-project

This repository includes a fundamental console-based application created with Python and Object-Oriented Programming (OOP) concepts for simple bank account management.

## I. Overview and Features of the Project

The system makes it easier to perform the fundamental tasks needed for a basic banking environment, such as creating user accounts, securely logging in, and processing financial transactions.

### Important Features:

* **Object-Oriented Design:** To guarantee modularity and concern separation, the architecture makes use of specialized `BankAcc` and `userManager` classes.
* **User-Accounts:** Facilitates the establishment of new user accounts, each of which is given a distinct 10-digit account number.
* **User Authentication:** Uses user ID and password verification to implement basic login functionality.
* **Transaction Processing:** Incorporates a class-level interest rate mechanism that can be applied to account balances.
* **Financial Logic:** Includes robust methods for `deposit` and `withdraw` operations, including validation checks for positive amounts and sufficient account funds.
* **Interface:** The user is guided through the available operations by a menu-driven, structured command-line interface.

## II. Technical Requirements

* **Programming Language:** Python 3.x or higher
* **Compiler:** Any python compiler

## III. Execution Instructions

1. **File Setup:** Store the given Python source code under the name `Bankmanager.py`.
2. System Installation: Enter the following command after navigating to the file's directory in your terminal or command prompt:


    ```bash
    python Bankmanager.py
    ```

## IV. System Utilization

When the system launches, it displays the Main Login/Creation Menu and initializes multiple accounts for testing.

* ** Initial Test Accounts:** * ID: `Harsh Singh`, Password: `123` * ID: `Shraddha Kapoor`, Password: `pass`
* **Main Operations:** After reading the Terms & Conditions, users have the option to **Log In** to an existing account, **Create New Account**, or **Exit System**.
* **Account Operations:** Users can examine their balance, make deposits, and make withdrawals after authenticating.

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

* **Bankmanager.py**: The primary Python source code file containing all class definitions (BankAcc, userManager) and the main program logic.
* **README.md**: The main documentation file, providing an overview of the project, features, and instructions for setup and running the system.
* **statement.md**: The design and architectural statement detailing the OOP structure, class responsibilities, and key design decisions.

<img width="1062" height="748" alt="image" src="https://github.com/user-attachments/assets/bbe0f5c3-07f4-48a6-a0c7-8e00c97b0174" />

<img width="736" height="839" alt="image" src="https://github.com/user-attachments/assets/c39b9218-1fc7-4884-9535-e7fce13133f1" />


