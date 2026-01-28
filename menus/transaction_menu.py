from services.transaction_actions import *
from read_write_files.write_transaction_details import write_transactions
from user_validation.user_details_validate import user_email


def transaction_menu():
  balance_amount = 0
    
  while True:

    print("1.Deposit \n2.Withdraw \n3.Transfer \n4.Balance \n5.Transaction History \n6.Prevoius Menu \n7.Exit")
    
    try:
        choice_for_Account_actions= int(input("Enter Your Choice : "))
        if choice_for_Account_actions > 7:
            raise ValueError("choose Between 6 choices")
        
    except Exception as e:
        print("Error : ",e)

    else:
      if choice_for_Account_actions == 1:
           email = user_email()
           balance_amount, deposit_amount , withdraw_amount   = deposit(balance_amount)
           write_transactions(email,deposit_amount,withdraw_amount,balance_amount)
           print("Your Amount is deposited Sucessfully ")

      elif choice_for_Account_actions == 2:
           email = user_email()
           balance_amount, deposit_amount , withdraw_amount = withraw(balance_amount)
           write_transactions(email,deposit_amount,withdraw_amount,balance_amount)
           print("Your Amount is Withdrawn Sucessfully")
      
      elif choice_for_Account_actions == 3:
           print(f"Current Balance : {balance_amount}")
      
      elif choice_for_Account_actions == 4:
          pass
      
      elif choice_for_Account_actions == 5:
          pass
      
      elif choice_for_Account_actions == 6:
          return
      
      else:
            print("You Exited This Menu")
            print("Thank You")
            return
      
      
      

      