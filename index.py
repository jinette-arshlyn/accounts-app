def check_balance():
    balance=get_balance() 
    print(f"Your balance is {balance}") 
    
def withdraw():
    amount=int(input("Enter amount to withdraw: "))
    balance=get_balance()
    if amount <= balance:
        print(f"Withdrawal successful. Your new balance is {balance - amount}")
    else:
        print("Insufficient funds.")