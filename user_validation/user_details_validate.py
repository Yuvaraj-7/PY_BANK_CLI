from datetime import datetime
import re
import getpass
from read_write_files.write_error import write_errorat_userdetails_to_log

"""i designed and coded  This Fuction as we are getting userinput from user only alphabets and convert it into lower 
but user input something which numbers we should throw error , i used isalpha to check whether all are alphabets
and recorded the error ocuur for future reference 
"""


def user_name():
    while True:
       try:
           Name = input("Enter Your name : ").strip().lower()
           if not Name:
               print("Username Cannot Be empty : Please  Enter Your name ")
               continue
           if not all(char.isalpha() or char == ' ' for char in Name):
                raise ValueError("Name Must contain Only Alphabets")
           return Name
       except Exception as e:
           write_errorat_userdetails_to_log(e)
           print("Name Should contain only Alphabets , Please Re enter Your name ")    





""" i designed and coded  This Fuction as we are getting userinput from user for our age as integer , as we should be above 18 to open saving bank account 
, i  given a raise og value error if user enter age less than 18 and asusual recorded the error in my log file,, i learned about all while designing this , where all condition 
are true then only wee met our requirement
"""   


"""def user_age():

    while True:
        try:
            Age = int(input("Enter Your Age : "))
            if not Age :
                print("Age Cannot Be empty : Please  Enter Your age ")
                continue
            if Age < 18:
                raise ValueError("You must be 18 years or above to open your saving Account ")
            return Age
        except Exception as e:
              write_errorat_userdetails_to_log(e)
              continue"""




""" i designed and coded  This Fuction as we are getting userinput from user  for our dob following format DD-MM-YYYY , 
removed spaces present anywhere in the string using strip function  , i checked for numbers and - , split the string by "-"
and stored the splitted parts used to validate using datetime function after converting our string to integers , set constrains for max and min ages , 
datetime() handles invalid dates.
"""


def user_dob():

    while True:
            DOB = input("Enter Your Date_of_Birth (DD-MM-YYYY) : ").strip()
            if not DOB:
                print("Date_of_Birth can not be empty")
                continue

            if not all(char.isdigit() or char == '-' for char in DOB):
                print("Your DOB Entry Contain other than numbers and - , Please Enter in Correct Format")
                continue

            split_DOB = DOB.split('-')
            if len(split_DOB) != 3:
                print("Date_of_Birth You Entered Is not in Correct Format Please Reenter Your DOB ")
                continue
            
            day_split, month_split ,year_split = split_DOB

            if len(day_split) != 2 or len(month_split) != 2 or len(year_split) != 4:
                print("Entered DOB is not in correct format , Please Follow(DD/MM/YYY)")
                continue

            try : 
                date = int(day_split)
                month = int(month_split)
                year = int(year_split)
            except ValueError:
                print("Day,Month,Year must be numbers")
                continue
            
            try:
                DOB_Validation = datetime(year,month,date)
            except ValueError as e :
                print("Invalid calendar date. Please enter a Correct date.")
                write_errorat_userdetails_to_log(e)
                continue

            current_year = datetime.now().year
            minimum_year = current_year - 18
           

            if year > minimum_year:
                print("Your Date_of_Birth doesnot match to our Policies")
                print("Please Re Enter Your Correct Age")
                continue
            
            return DOB 
    


def user_age(DOB):
    split_DOB = DOB.split('-')
    day_split, month_split ,year_split = split_DOB
    date_check_age = int(day_split)
    month = int(month_split)
    year = int(year_split)
    current_year = datetime.now().year
    Age = current_year - year
    return Age

""" 
i designed and coded  This Fuction as we are getting userinput from user only alphabets and convert it into lower andemoved spaces
used not in function to check and compare our input and required input and recorded error 
"""


def user_gender():

 while True:
    try:
       Gender = input("Enter Your Gender(m/male , f/female , N/rathernottosay : ").strip().lower()
       if not Gender:
           print("Genter Cannot be empty")
           continue
       if Gender not in ["m","male","f","female","n","rathernottosay"]:
           raise ValueError("Please Enter Correct input , follow (m/male , f/female , N/rathernottosay)")
       return Gender
    except Exception as e:
         write_errorat_userdetails_to_log(e)
         




""" i designed and coded  This Fuction as we are getting userinput from user of our mobile no and check that all entered input are 
digits using isdigit() and length of our mobile number should be 10 and the first number of our mobile number shd be 9/8/7/6 and recorded error in our log file
"""


def user_mobile_no():
   
 while True:
     try:
        mobile = input("Enter Your 10 digit Mobile number : ")
        if not mobile:
            print("Mobile no cannot be Empty ")
            continue
        if not (mobile.isdigit() and len(mobile) == 10 and mobile[0] in ["6","7","8","9"]):
            print("Please Enter Your Correct Mobile Number ")
            continue
        return mobile
     except Exception as e:
          write_errorat_userdetails_to_log(e)






"""
i designed and coded  This Fuction as we are getting userinput from user of our email, i learned about regrex function while coding 
imported re module and compare the pattern and our emailid and also recorded the error 
"""



def user_email():
       
       while True :
        try:
           email = input("Enter Your email : ")
           email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
           if not email:
               print("email cannot be empty")
               continue
           if not re.match(email_pattern,email):
                print("Please Enter Your Correct Mail_id")
                continue
           return email
        except Exception as e:
              write_errorat_userdetails_to_log(e)






"""
i designed and coded  This Fuction as we are getting userinput from user of our password used the regrex function here also 
and i made the password invisible using getpass by importing getpass module , matched my regrex pattern of password with 
my password , i also added other layer of password protection like confirm password

"""



def user_password():
     
    while True: 
      try:
        Password = getpass.getpass("Enter your password (invisible) (min 8character , max 15characters): ")
        if not Password:
           print("Password Cannot be empty")
           continue

        password_pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,15}$'

        if not re.match(password_pattern, Password):
           print("Password Should Have Atleast 1caps , 1specialcharacter , 1number ")
        confirm_password =  getpass.getpass("Confirm password (invisible) (min 8character , max 15characters): ")
        if not confirm_password:
           print("Please Confirm Your Password")
           continue
        if Password != confirm_password:
            print("Your Passord Doesnot matches while confirming , Please reenter password")
            continue
        if len(Password) < 8 and len(Password) > 15:
            print("Your Password Length Voilates The our Constrains")
            continue
        return Password
      except Exception as e:
          write_errorat_userdetails_to_log(e)
          

        



    