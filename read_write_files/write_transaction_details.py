import csv
import os
from user_validation.user_details_validate import *
from services.transaction_actions import *



def write_transactions(email, deposit_amount, withdraw_amount, balance):

    filename = "user_transaction_details.csv"
    file_exists = os.path.exists(filename)

    fields = ["User_name","User_mail","Acc_No.","deposit_amount","withdraw_amount","balance"]

    with open("user_account_details.csv", "r", newline="") as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for i in csv_reader:
            if i["User_mail"] == email:

                with open(filename, "a", newline="") as f:
                    csv_writer = csv.DictWriter(f, fieldnames=fields)

                    if not file_exists:
                        csv_writer.writeheader()

                    csv_writer.writerow({
                        "User_name": i["User_name"],
                        "User_mail": i["User_mail"],
                        "Acc_No.": i["Acc_No."],
                        "deposit_amount": deposit_amount,
                        "withdraw_amount": withdraw_amount,
                        "balance": balance
                    })

                return