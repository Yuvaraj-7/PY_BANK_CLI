import secrets
import csv
import os

"""
This function , i am going to create account no , account type , account ifsc code and branch name 
after the user created account ,there details we have in user_details right , so i read this file get email , 
username and generate the acc no , ifsc code , and write the the generated in to the file user_account_details .
i also print the user details.

"""


def account_details():
          with open("user_details.csv","r") as csv_file:
                  csv_reader = csv.DictReader(csv_file)
                  for i in csv_reader:
                          user_name_readed = i["Name"]
                          user_mail_reader = i["email"]
                          user_DOB_reader = i["DOB"]
                          account_number = secrets.randbelow((10**15 - 10**14)+10**14)
                          with open("user_account_details.csv","r") as csv_file:
                                  csv_reader = csv.DictReader(csv_file)
                                  for i in csv_reader:
                                     account_number_reader = i["Acc_No."]
                                     if account_number_reader == account_number:
                                           continue
                          account_type = "Savings"
                          account_ifsc = "ERTPS"+ user_DOB_reader
                          account_branch = "$AVE$ BANk , THIRUPPUR , ERODE - 600123"
                          file_exists= os.path.exists("user_account_details.csv")
                          fields=["User_name","User_mail","Acc_No.","Acc_Type","Acc_IFSC","Acc_Branch"]
                          with open("user_account_details.csv","a") as f:
                            csv_writer = csv.DictWriter(f,fieldnames=fields)
                            if not file_exists:
                                 csv_writer.writeheader()
                            csv_writer.writerow({
                                    "User_name": user_name_readed,
                                    "User_mail": user_mail_reader ,
                                    "Acc_No.": account_number,
                                    "Acc_Type":  account_type,
                                    "Acc_IFSC": account_ifsc,
                                    "Acc_Branch": account_branch,
                                    
                                })
                  print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                  print(f"     User_name                 User_mail                Acc_No.                   Acc_type                             Acc_IFSC                                                          Acc_Branch                          ")                                                                                               
                  print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                  print(f" {user_name_readed}        {user_mail_reader}           {account_number}            {account_type}                   {account_ifsc}                                           {account_branch} ")  
                                
                  return user_name_readed,user_mail_reader, account_number , account_type , account_ifsc , account_branch
        