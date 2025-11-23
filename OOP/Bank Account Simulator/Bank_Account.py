import random
class Bank_Account:
    """Creating the class that all bank account objects will inherit from"""
    def __init__(self,Account_Name:str):
        self.Account_Name = Account_Name
        self.Account_Number = self.generate_account_number()
        self.Balance = 0
    
    def generate_account_number(self):
        """This method creates a user's account number """
        user_number = str(random.randint(0,300))
        account_number = "114" + user_number
        return account_number
    
    def deposit(self,amount:int):
        """This method adds to the account balance"""
        self.Balance += amount
        print("Amount Successfully Deposited")
        return True
    
    def withdraw(self,amount:int):
        """This method deducts from the account balance"""
        if amount > self.Balance:
            return False
        elif self.Balance == 0:
            return False
        else:
             self.Balance -= amount
             print("Amount Successfully Withdrawn")
             return True
            

    def get_balance(self):
        """This method returns the account balance"""
        return self.Balance



