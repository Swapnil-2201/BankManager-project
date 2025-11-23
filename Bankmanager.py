import random



class BankAcc:
    _int_rate=0.02
    def __init__(self,ownr,initbal=0):
            if(initbal<0):raise ValueError("Initial balance cannot be negatiive.")
            self.owner_name=ownr
            self.bal_amt=float(initbal)
            self.acno=self._g()
    def deposit(self,a):
       if a>0:
            self.bal_amt+=a;return True
       return False
    def withdraw(self,a):
       if(a<=0):
        return False,"Withdrawal ammount must be positive."
       if a>self.bal_amt:
            return False,"Insufficient funds! Withdrawal cancelled."
       self.bal_amt-=a;return True,"Withdrawal successful."
    @property
    def bal(self):return self.bal_amt
    def apply_interest(self):
          x=self.bal_amt*BankAcc._int_rate;self.bal_amt+=x;return x
    @classmethod
    def set_int_rate(cls,r):
     if 0<=r<=1:
      cls._int_rate=r;return True
     return False
    @staticmethod
    def _g():
       z=''
       for q in range(10):z+=str(random.randint(0,9))
       return z



class userManager:
     UD={} 

     @classmethod
     def create_acc(cls,u,p,i):
          if u in cls.UD:
                print("Error: Thiis User ID '"+u+"' alreadyy exists.");return False
          a=BankAcc(u,i)
          cls.UD[u]={'password':p,'account':a}
          print(f"User '{u}' created successfully with Bank Account No. {a.acno}.");return True

     @classmethod
     def login(cls,u,p):
         if u not in cls.UD:print("Error: User ID not found.");return None
         d=cls.UD[u]
         if d["password"]==p:
              print("Login successfull for user: "+u);return d["account"]
         print("Error: Incorrect password.");return None




def stats(acct) :
    
   print("\n... Account Statistics ...")
   print("Owner: ", acct.owner_name if hasattr(acct,"owner_name") else acct.owner_name )
   print("Account No:  " + str(acct.acno))

   bal_str = format(acct.bal_amt ,",.2f")
   print("Current Balance: ₹" + bal_str)

   ir = BankAcc._int_rate * 100
   print("Interest Rate:", ("%0.2f" % ir) + "%")


def UI_loop(ac) :
     while(True):
        stats( ac )
        print("\n--- User Actions ----")
        print("1.Deposit")
        print("2.  Withdraw")
        print("3. Log   Out ")
        c = input("Select an action (1-3): ").strip()

        if c == "1" :
            try:
                v = float(input("Enter deposit amount: ₹ ").strip())
                okk = ac.deposit(v)
                if(okk):
                    print("Successfully deposited ₹" + str(format(v,".2f")) )
                else:
                    print("Deposit failed. Ammount must be positive")
            except:
                print("Invalid input. Please enter a valid numm")     

        elif c   ==  "2" :
            try:
                w = float(input("Enter withdrawal amount: ₹"))
                rr = ac.withdraw(w)
                print(rr)
            except:
                print("Invalid input. Please enter a valid numm.")
        elif c == "3":
            print("Logging outt ... ")
            break        
        else :
            print("Invalid choice...   try again maybe.")



def display_tc():
    print("\n........................................................")
    print("      Bank Account Terms and Conditions       ")
    print(".........................................................")
    print("1. ACCOUNT OWNERSHIP: You must be 18 years & Above.")
    print("2. DATA PRIVACY: Security of your data is our top-most prioriity.")
    print("3. INTEREST RATE: The current rate is "+format(BankAcc._int_rate*100,".2f")+"% and is subject to change.")
    print("4. WITHDRAWAL LIMITS: You are responsible for maintaining a positive balance.")
    print("........................................................\n")
    r=input("Do you agree to the Terms and Conditions? (Y/N): ").strip().upper()
    return r=="Y"




if __name__=="__main__":

 print("... Bank Manager Initialization ...")
 userManager.create_acc("Harsh Singh","123",500000.00)
 userManager.create_acc("Shraddha kapoor","pass",12000000.50)
 userManager.create_acc("Amitabh Bachchan","abc123",750000.75)
 userManager.create_acc("Deepika Padukone","qwerty",300000.00)
 print("\n")

 while True:
  print("... Main Login/Creation Menu ...")
  print("1. Log In")
  print("2. Create New Account")
  print("3. View T&C")
  print("4. Exit System")
  x=input("Enter your choice (1-4): ")
  if x=="1":
        u=input("User ID: ");pw=input("Password: ")
        acc=userManager.login(u,pw)
        if acc:UI_loop(acc)
  elif x=="2":
        print("\n... New Account Registration ...")
        if not display_tc():
             print("Account creation was cancelled. T&C must be accepted.");continue
        nid=input("Create an User ID: ")
        npw=input("Create a Password: ")
        try:
             nb=float(input("Enter initial deposit amount (₹0 min): "))
             if nb<0:print("Initial deposit can't be negatiive. Creation was failed.");continue
             userManager.create_acc(nid,npw,nb)
        except:
             print("Invalid amount entered. Creation was failed.")
  elif x=="3":
        display_tc()
  elif x=="4":
        print("Logged Out Successfully. Goodbye!")
        break
  else:print("Invalid option. Please try again.")


#Abbreviations:
#ac - account 
#amt - amount 
#bal - balance
#dep - deposit
#int_rate - interest rate
#nid - new user id
#npw - new password
#UD - user database
