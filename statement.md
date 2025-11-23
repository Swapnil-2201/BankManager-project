# Bank Account Management System: Project Statement

This document outlines the core purpose, boundaries, intended audience, and main features of the Bank Account Management System.

---

## 1. Problem Statement

The goal is to address the need for a **simple, simulated environment** to practice and demonstrate **Object-Oriented Programming (OOP)** principles in Python. The challenge is to model real-world banking entities and processes (accounts, transactions, user management) in a structured and maintainable way, ensuring data encapsulation and logical separation of concerns. The system must provide a reliable foundation for testing basic financial and authentication logic.

## 2. Scope of the Project

The scope of this project is strictly limited to a **console-based application** focused on internal account management logic.

### In Scope:

* Creating and storing user accounts with associated passwords.
* Basic financial transactions: Deposit and Withdrawal.
* Validation for transaction amounts and insufficient funds.
* Application of a static, class-level interest rate.
* Menu-driven navigation and console output.

### Out of Scope:

* Persistence (Database storage). All user data is volatile and stored in memory (`ClassVar[Dict]`).
* Advanced security features (e.g., encryption, multi-factor authentication).
* Handling multiple currencies or complex loan/investment products.
* Web or Graphical User Interface (GUI) development.

## 3. Target Users

The system is designed primarily for two audiences:

| Target User | Primary Use Case |
| :--- | :--- |
| **Developers/Students** | To study and demonstrate OOP concepts, class design, and method structure in a practical, real-world scenario (banking simulation). |
| **System Testers** | To quickly test core financial logic (deposits, withdrawals, balance checks) through a simple command-line interface. |

## 4. High-Level Features

The following are the main functionalities provided by the system:

* **Account Initialization:** Ability to create a new user account by setting a User ID, Password, and initial deposit amount.
* **Secure Authentication:** A login mechanism that validates credentials (User ID and Password) against the stored user data.
* **Funds Deposit:** Allows the user to add a positive amount to their current account balance.
* **Funds Withdrawal:** Allows the user to remove funds, provided the amount is positive and does not exceed the current balance.
* **Account Status Display:** Provides real-time statistics, including the current balance, owner name, and account number.
