import csv
from user_validation.user_details_validate import *
from menus.update_menu import *
# i learned about circulasr import deadlock here 

"""
this function is for update menu , we create a empty list which will allocates memory ,we ask what they want 
to change email/mobileno/password whatever they chhose ,we get email , password to get the user details , if our readed mail
matches with recieved mail and same for password then the changes performed all data readed , will append and our modified
data will also append and we write into the user details , in write mode , because old data will be erased.
if email not found we will say no account exists like that

"""




def update_mobile_no(email,new_mobile):
    rows = []
    updated = False
    with open("user_details.csv","r",newline="") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        fieldnames = csv_reader.fieldnames
            
        for row in csv_reader:
            if row["email"] == email:
                row["mobile"] = new_mobile
                updated = True
            rows.append(row)
    if updated:
        with open("user_details.csv", "w", newline="") as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writeheader()
            csv_writer.writerows(rows)
        print(" Mobile number updated successfully!")
    else:
        print(" Email not found. No update performed.")


def update_email(email,new_email):
    rows = []
    updated = False
    with open("user_details.csv","r",newline="") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        fieldnames = csv_reader.fieldnames
            
        for row in csv_reader:
            if row["email"] == email:
                row["email"] = new_email
                updated = True
            rows.append(row)
    if updated:
        with open("user_details.csv", "w", newline="") as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writeheader()
            csv_writer.writerows(rows)
        print(" Email  updated successfully!")
    else:
        print(" Email not found. No update performed.")




def update_password(email,Password,passwrd):
    rows = []
    updated = False
    with open("user_details.csv","r",newline="") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        fieldnames = csv_reader.fieldnames
            
        for row in csv_reader:
            if row["email"] == email and row["Password"]== passwrd:
                row["Password"] = Password
                updated = True
            rows.append(row)
    if updated:
        with open("user_details.csv", "w", newline="") as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writeheader()
            csv_writer.writerows(rows)
        print(" Password changed successfully!")
    else:
        print(" Email not found. No update performed.")