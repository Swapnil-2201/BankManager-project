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

## V. Repository Structure

* **Bankmanager.py**: The primary Python source code file containing all class definitions (BankAccount, UserManager) and the main program logic.
* **README.md**: The main documentation file, providing an overview of the project, features, and instructions for setup and running the system.
* **statement.md**: The design and architectural statement detailing the OOP structure, class responsibilities, and key design decisions.
