from user_validation.user_details_validate import user_email , user_mobile_no ,user_password
from services.update_user_details import update_mobile_no , update_email , update_password
from services.account_actions import account_details


"""
This menu is a part of account menu(choice 2) , This deals with upadating mobile no , email , changing paasword
the related functions i created in update user details . 
"""

def update_user_details_menu():

 while True:
    print("1.Update Mobile No.\n2.Update Email address \n3.Reset password \n4.Previous Menu(Account_Details) \n5.Exit")
    try:
        choice_for_update = int(input("Enter Your Choice : "))
        if  choice_for_update < 1 or choice_for_update > 5:
            raise ValueError("choose Between  choices")
        
    except Exception as e:
        print("Error : ",e)
        return

    else:
        if choice_for_update == 1:
            email = user_email()
            print("Enter New Mobile number")
            new_mobile = user_mobile_no()
            update_mobile_no(email,new_mobile)

        elif choice_for_update == 2:
            email = user_email()
            print("Enter New Mail id")
            new_email = user_email()
            update_email(email,new_email)

        elif choice_for_update == 3:
            email = user_email()
            print("Enter Your Old Password and confirm it")
            passwrd = user_password()
            print("Enter Your new Password and Confirm It")
            Password = user_password()
            update_password(email,Password,passwrd)

        elif choice_for_update == 4:
           print("To View Your Account Details")
           account_details()

        elif choice_for_update == 5:
            print("You Exitted Current Menu")
            print("Thank You !")
            return

        else:
            continue
            
           

            



           