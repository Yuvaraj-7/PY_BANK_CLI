from user_validation.user_details_validate import *
from read_write_files.write_user_detail import write_userdetails

"""
This function i designed for main menu , i already  designed functions for user details with constrains i imported and
called all the functions and stored the return values  and passed as a argument for the write file , this menu has 
2 choices "1. Create Account and 2. Login" . login we collect email and password as arguments for checking user
is already present or not in readfiles.
"""


def signup():
    print("1. Create Account \n2. Login")

    try:
        choice_for_login = int(input("Enter Your Choice : "))
        if choice_for_login > 2:
            raise ValueError("choose Between 2 choices")
        
    except Exception as e:
        print("Error : ",e)

    else:
        if choice_for_login == 1:
            Name = user_name()
            Age = user_age()
            DOB =  user_dob()
            Gender = user_gender()
            mobile =  user_mobile_no()
            email =  user_email()
            Password = user_password()
            write_userdetails(Name,Age,DOB,Gender,mobile,email,Password)
           

        else:
            pass
