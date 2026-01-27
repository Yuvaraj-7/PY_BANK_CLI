import csv



"""
This Function is used to  check that our user when user enter create account details  from maimenu (choice1) whether the user is already
having account in our bank and again trying to create account with same details  . we are gettin user input  for email and password ,
confirm it stroing in a variable and passing as argument for this function i called in main menu. In this file 
i passed the arguments that stored and i reading file for key email , if email matches with entered email we print
You already have account message else we proceed with writing the details in to csv user_details file .
"""

def account_already_exists_ornot(email,Password):
    with open("user_details.csv","r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for i in csv_reader:
            email_readed = i["email"]
            Password_readed = i["Password"]
            if email == email_readed and Password == Password_readed:
                return True
            