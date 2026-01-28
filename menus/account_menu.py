from services.account_actions import *
from menus.account_menu import *
from menus.update_menu import update_user_details_menu
from menus.transaction_menu import transaction_menu




""" 
This function i designed for  showing account action menu "1 View Account Details 2.Update account info 3. Exit"
"""


def account_menu():

  while True:

    print("1 View Account Details \n2.Update account info \n3.Transaction Menu \n4. Exit")
    
    try:
        choice_for_Account_actions= int(input("Enter Your Choice : "))
        if choice_for_Account_actions > 4:
            raise ValueError("choose Between 4 choices")
        
    except Exception as e:
        print("Error : ",e)

    else:
      if choice_for_Account_actions == 1:
           account_details()

      elif choice_for_Account_actions == 2:
          update_user_details_menu()

      elif choice_for_Account_actions == 3:
          transaction_menu()
          

      else:
            print("You Exited This Menu")
            print("Thank You")
            return
            