import random



class BankAccount:
    _interest_rate=0.02
    def __init__(self,ownr,initbal=0):
            if(initbal<0):raise ValueError("Initial balance cannot be negative.")
            self.owner_name=ownr
            self.balance_amt=float(initbal)
            self.acno=self._g()
    def deposit(self,a):
       if a>0:
            self.balance_amt+=a;return True
       return False
    def withdraw(self,a):
       if(a<=0):
        return False,"Withdrawal amount must be positive."
       if a>self.balance_amt:
            return False,"Insufficient funds! Withdrawal cancelled."
       self.balance_amt-=a;return True,"Withdrawal successful."
    @property
    def balance(self):return self.balance_amt
    def apply_interest(self):
          x=self.balance_amt*BankAccount._interest_rate;self.balance_amt+=x;return x
    @classmethod
    def set_interest_rate(cls,r):
     if 0<=r<=1:
      cls._interest_rate=r;return True
     return False
    @staticmethod
    def _g():
       z=''
       for q in range(10):z+=str(random.randint(0,9))
       return z



class UserManager:
     _user_data={}

     @classmethod
     def create_user_account(cls,u,p,i):
          if u in cls._user_data:
                print("Error: User ID '"+u+"' already exists.");return False
          a=BankAccount(u,i)
          cls._user_data[u]={'password':p,'account':a}
          print(f"User '{u}' created successfully with Bank Account No. {a.acno}.");return True

     @classmethod
     def login(cls,u,p):
         if u not in cls._user_data:print("Error: User ID not found.");return None
         d=cls._user_data[u]
         if d["password"]==p:
              print("Login successful for user: "+u);return d["account"]
         print("Error: Incorrect password.");return None




def display_user_stats(a):
 print("\n--- Account Statistics ---")
 print("Owner:",a.owner_name)
 print("Account No:",a.acno)
 print("Current Balance: $"+format(a.balance_amt,",.2f"))
 print("Interest Rate: "+format(BankAccount._interest_rate*100,".2f")+"%")
 print("--------------------------")



def user_interface_loop(ac):
      while True:
       display_user_stats(ac)
       print("\n--- User Actions ---")
       print("1. Deposit")
       print("2. Withdraw")
       print("3. Log Out")
       c=input("Select an action (1-3): ")
       if c=="1":
            try:
                 v=float(input("Enter deposit amount: ₹"))
                 if ac.deposit(v):print("Successfully deposited ₹"+format(v,".2f"))
                 else:print("Deposit failed. Amount must be positive.")
            except:print("Invalid input. Please enter a number.")
       elif c=="2":
            try:
                 w=float(input("Enter withdrawal amount: ₹"))
                 ok,msg=ac.withdraw(w);print(msg)
            except:
                 print("Invalid input. Please enter a number.")
       elif c=="3":
            print("Logging out...");break
       else:print("Invalid choice. Please try again.")



def display_terms_and_conditions():
    print("\n==============================================")
    print("      Bank Account Terms and Conditions       ")
    print("==============================================")
    print("1. ACCOUNT OWNERSHIP: You must be 18 years or older.")
    print("2. DATA PRIVACY: Your data is protected by strict internal policies.")
    print("3. INTEREST RATE: The current rate is "+format(BankAccount._interest_rate*100,".2f")+"% and is subject to change.")
    print("4. WITHDRAWAL LIMITS: You are responsible for maintaining a positive balance.")
    print("==============================================")
    r=input("Do you agree to the Terms and Conditions? (Y/N): ").strip().upper()
    return r=="Y"




if __name__=="__main__":

 print("--- Bank Manager Initialization ---")
 UserManager.create_user_account("Harsh Singh","123",500000.00)
 UserManager.create_user_account("Shraddha kapoor","pass",12000000.50)
 UserManager.create_user_account("Amitabh Bachchan","abc123",750000.75)
 UserManager.create_user_account("Deepika Padukone","qwerty",300000.00)
 print("\n")

 while True:
  print("--- Main Login/Creation Menu ---")
  print("1. Log In")
  print("2. Create New Account")
  print("3. View T&C")
  print("4. Exit System")
  x=input("Enter your choice (1-4): ")
  if x=="1":
        u=input("User ID: ");pw=input("Password: ")
        acc=UserManager.login(u,pw)
        if acc:user_interface_loop(acc)
  elif x=="2":
        print("\n--- New Account Registration ---")
        if not display_terms_and_conditions():
             print("Account creation cancelled. T&C must be accepted.");continue
        nid=input("Choose a User ID: ")
        npw=input("Choose a Password: ")
        try:
             nb=float(input("Enter initial deposit amount (₹0 min): "))
             if nb<0:print("Initial deposit cannot be negative. Creation failed.");continue
             UserManager.create_user_account(nid,npw,nb)
        except:
             print("Invalid amount entered. Creation failed.")
  elif x=="3":
        display_terms_and_conditions()
  elif x=="4":
        print("System shutting down. Goodbye!")
        break
  else:print("Invalid option. Please try again.")
