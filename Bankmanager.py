import random
from typing import ClassVar, Dict, Any

class BankAccount:
    _interest_rate: ClassVar[float] = 0.02
    
    def __init__(self, owner: str, initial_balance: float = 0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self._owner = owner
        self._balance = initial_balance
        self._account_number = BankAccount.generate_account_number()

    @property
    def balance(self) -> float:
        return self._balance

    @property
    def owner(self) -> str:
        return self._owner

    @property
    def account_number(self) -> str:
        return self._account_number

    def deposit(self, amount: float):
        if amount > 0:
            self._balance += amount
            return True
        return False

    def withdraw(self, amount: float):
        if amount <= 0:
            return False, "Withdrawal amount must be positive."
        if amount > self._balance:
            return False, "Insufficient funds! Withdrawal cancelled."
        
        self._balance -= amount
        return True, "Withdrawal successful."

    def apply_interest(self):
        interest_earned = self._balance * BankAccount._interest_rate
        self._balance += interest_earned
        return interest_earned

    @classmethod
    def set_interest_rate(cls, new_rate: float):
        if 0 <= new_rate <= 1:
            cls._interest_rate = new_rate
            return True
        return False

    @staticmethod
    def generate_account_number() -> str:
        return ''.join([str(random.randint(0, 9)) for _ in range(10)])

class UserManager:
    _user_data: ClassVar[Dict[str, Dict[str, Any]]] = {}

    @classmethod
    def create_user_account(cls, user_id: str, password: str, initial_balance: float) -> bool:
        if user_id in cls._user_data:
            print(f"Error: User ID '{user_id}' already exists.")
            return False
        
        cls._user_data[user_id] = {
            'password': password,
            'account': BankAccount(owner=user_id, initial_balance=initial_balance)
        }
        print(f"User '{user_id}' created successfully with Bank Account No. {cls._user_data[user_id]['account'].account_number}.")
        return True

    @classmethod
    def login(cls, user_id: str, password: str) -> BankAccount | None:
        if user_id not in cls._user_data:
            print("Error: User ID not found.")
            return None
        
        user_info = cls._user_data[user_id]
        if user_info['password'] == password:
            print(f"Login successful for user: {user_id}")
            return user_info['account']
        else:
            print("Error: Incorrect password.")
            return None

def display_user_stats(account: BankAccount):
    print("\n--- Account Statistics ---")
    print(f"Owner: {account.owner}")
    print(f"Account No: {account.account_number}")
    print(f"Current Balance: ${account.balance:,.2f}")
    print(f"Interest Rate: {BankAccount._interest_rate*100:.2f}%")
    print("--------------------------")

def user_interface_loop(account: BankAccount):
    while True:
        display_user_stats(account)
        print("\n--- User Actions ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Log Out")
        
        choice = input("Select an action (1-3): ")
        
        if choice == '1':
            try:
                amount = float(input("Enter deposit amount: $"))
                if account.deposit(amount):
                    print(f"Successfully deposited ${amount:.2f}.")
                else:
                    print("Deposit failed. Amount must be positive.")
            except ValueError:
                print("Invalid input. Please enter a number.")
                
        elif choice == '2':
            try:
                amount = float(input("Enter withdrawal amount: $"))
                success, message = account.withdraw(amount)
                print(message)
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == '3':
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

def display_terms_and_conditions() -> bool:
    """Displays mock T&C and prompts for acceptance."""
    print("\n==============================================")
    print("      Bank Account Terms and Conditions       ")
    print("==============================================")
    print("1. ACCOUNT OWNERSHIP: You must be 18 years or older.")
    print("2. DATA PRIVACY: Your data is protected by strict internal policies.")
    print(f"3. INTEREST RATE: The current rate is {BankAccount._interest_rate*100:.2f}% and is subject to change.")
    print("4. WITHDRAWAL LIMITS: You are responsible for maintaining a positive balance.")
    print("==============================================")
    
    acceptance = input("Do you agree to the Terms and Conditions? (Y/N): ").upper()
    return acceptance == 'Y'


if __name__ == "__main__":
    print("--- Bank Manager Initialization ---")
    
    UserManager.create_user_account("Harsh Singh", "123", 500000.00)
    UserManager.create_user_account("Shraddha kapoor", "pass", 12000000.50)
    UserManager.create_user_account("Amitabh Bachchan", "bigb", 7500000.75)
    UserManager.create_user_account("Deepika Padukone", "dp", 3000000.00)
    print("\n")
    
    while True:
        print("--- Main Login/Creation Menu ---")
        print("1. Log In")
        print("2. Create New Account")
        print("3. View T&C")
        print("4. Exit System")
        main_choice = input("Enter your choice (1-4): ")
        
        if main_choice == '1':

            user_id = input("User ID: ")
            password = input("Password: ")
            
            logged_in_account = UserManager.login(user_id, password)
            
            if logged_in_account:
                user_interface_loop(logged_in_account)
                
        elif main_choice == '2':

            print("\n--- New Account Registration ---")

            if not display_terms_and_conditions():
                print("Account creation cancelled. T&C must be accepted.")
                continue

            new_id = input("Choose a User ID: ")
            new_pass = input("Choose a Password: ")
            try:
                initial = float(input("Enter initial deposit amount ($0 min): "))
                if initial < 0:
                    print("Initial deposit cannot be negative. Creation failed.")
                    continue
                UserManager.create_user_account(new_id, new_pass, initial)
            except ValueError:
                print("Invalid amount entered. Creation failed.")
                
        elif main_choice == '3':
            display_terms_and_conditions()
            
        elif main_choice == '4':
            print("System shutting down. Goodbye!")
            break
            
        else:
            print("Invalid option. Please try again.")