import csv
import os
from user_validation.user_details_validate import *

""" 
This function i used to write my user entered values in to file user_details ,while creating the account,
i prefered dictionary format here , i thought i can easyly acess values through keys and value pair . 
write as rows with field names Name,Age,DOB,Gender,mobile,email,Password.
"""

def write_userdetails(Name,Age,DOB,Gender,mobile,email,Password):
    filename = "user_details.csv"
    file_exists= os.path.exists(filename)
    fields=["Name","Age","DOB","Gender","mobile","email","Password"]
    with open(filename,"a",newline="") as f:
        csv_writer = csv.DictWriter(f,fieldnames=fields)
        if not file_exists:
            csv_writer.writeheader()
        csv_writer.writerow({
            "Name": Name,
            "Age": Age,
            "DOB": DOB,
            "Gender": Gender,
            "mobile": mobile,
            "email": email,
            "Password": Password
        })
    print("Account Created Successfully")


    
    
        