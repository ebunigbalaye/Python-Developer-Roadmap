import Bank
digi_bank = Bank.Bank()
running = True
while running:
    print("""Welcome to the Digital Bank
1. Create new account
2. Deposit money
3. Withdraw money
4. Check balance
5. Transfer money
6. Exit""")
    action = input("Enter the action you would like to perform: ")
    if action == "1":
        account_name = input("Enter the account name: ")
        account = digi_bank.create_account(account_name)
        print(f"Account Created Successfully with account number {account.Account_Number}")

    elif action == "2" :
        account_number = input ("Enter the account number of the account you would like to deposit money to: ")
        amount = int( input("Enter the amount you'd like to deposit: "))
        digi_bank.deposit_to(account_number,amount)
        

    elif action == "3" :
        account_number = input ("Enter the account number of the account you would like to withdraw money from: ")
        amount = int( input("Enter the amount you'd like to withdraw: "))
        digi_bank.withdraw_from(account_number,amount)
        

    elif action == "4":
        account_number = input("Enter your account number: ")
        print(digi_bank.check_balance(account_number))

    elif action == "5" :
        sender_account_number = input("Enter the account number you're transferring from: ")
        receiver_account_number = input("Enter the account number you're transferring to: ")
        amount = int(input("Enter the amount you would like to transfer: "))
        print(digi_bank.transfer(sender_account_number,receiver_account_number,amount))

    else:
        running = False