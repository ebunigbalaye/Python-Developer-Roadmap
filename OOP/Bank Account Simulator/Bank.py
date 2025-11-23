from Bank_Account import Bank_Account
class Bank:
    """DCreating The Bank Class that all bank objects will inherit from"""
    def __init__(self):
        self.accounts = []
    def create_account(self,user_name):
        """This method creates an account object given the user's name"""
        user_account = Bank_Account(user_name)
        self.accounts.append(user_account)
        return user_account
    def get_account(self,account_number):
        """This method fetches the account object using the acount_number as input"""
        for i in self.accounts:
            if i.Account_Number == account_number:
                return i
          
            
    def deposit_to(self,account_number:str,amount:int):
        """This methods adds to the balance of an account"""
        account = self.get_account(account_number) 
        if account == None:
            print("Account not Found")
        else:
            account.deposit(amount)
            print("Amount Successfully Deposited")
    
    def withdraw_from(self,account_number:str,amount:int):
        """This method subtracts from the balance attribute of an account"""
        account = self.get_account(account_number) 
        print(account)
        if account == None:
            print ("Account Not Found")
        else:
           account.withdraw(amount)
           print("Amount Successfully Withdrawn")

    def check_balance(self,account_number:str):
        """This method returns the balance of an account"""
        account = self.get_account(account_number) 
        if account == None:
            return ("Account Not Found")
        else:
            return account.get_balance()
    
    def transfer(self,sender_account_number,receiver_account_number,amount):
        """This method transfers money between accounts"""
        sender_account = self.get_account(sender_account_number) 
        receiver_account = self.get_account(receiver_account_number) 

        if receiver_account == None :
            return ("Invalid Receiver Account")
        elif sender_account == None:
            return("Invalid Sender Account")

        
        if sender_account.withdraw(amount) :
           receiver_account.deposit(amount) 
           return("Amount Transferred Successfully")
        else:
            return ("Transfer Failed. Insufficient Balance")
       

    

