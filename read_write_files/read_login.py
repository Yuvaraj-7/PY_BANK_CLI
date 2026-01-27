import csv
"""
This Function is used to  check that our user when user enter login from maimenu whether the user is already
having account in our bank or not . we are gettin user input  for email and password ,
confirm it stroing in a variable and passing as argument for this function i called in main menu. In this file 
i passed the arguments that stored and i reading file for key email , if email matches with entered email we print
welcome back message else we indicate that user is not present .
"""

def read_user_details(email,Password):
    with open("user_details.csv","r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for i in csv_reader:
            user_readed = i["Name"]
            email_readed = i["email"]
            Password_readed = i["Password"]
            if email == email_readed and Password == Password_readed:
                print(f"Welcome  Back {user_readed} ! ")
                return True
            else :
               print("You Dont Have Account , Please Create account to proceed")
               return False
                