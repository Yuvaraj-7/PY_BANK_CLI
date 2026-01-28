

def deposit(balance_amount):
    try :
        deposit_amount = float(input("Enter The Amount You need to deposit : "))
        if deposit_amount <= 0:
            raise ValueError("Deposit Amount Cannot Be Zero  / negative")
        balance_amount += deposit_amount
        return balance_amount , deposit_amount ,0
    except Exception as e:
        print(f"Error : {e}")
        return balance_amount , 0 ,0
        
        
    

def withraw(balance_amount):
    try :
        withdraw_amount = float(input("Enter The Amount You need to Withdraw : "))
        if withdraw_amount <= 0:
            raise ValueError("Withraw element cannot be Zero")
        if withdraw_amount > balance_amount:
            raise ValueError("Withdraw Amount Cannot more than Balance amount")
        balance_amount -= withdraw_amount
        return balance_amount , 0 ,withdraw_amount
    except Exception as e:
        print(f"Error : {e}")
        return balance_amount , 0 ,0


   
    