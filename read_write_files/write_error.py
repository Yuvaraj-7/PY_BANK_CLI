from datetime import datetime


def write_errorat_userdetails_to_log(e):
     filename = "user_data_errors.log"
     with open(filename,"a",newline="") as log:
                 log.write(f"This Error occur at user input @ userdetails  {datetime.now()} | {type(e).__name__} | {e}\n") 
                 print(e)