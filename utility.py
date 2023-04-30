"""
Project 2 Team 1
Matthew McNatt: 1001739201
Vladimir Caterov: 1002011907
Harrison Cawood: 1001729180
Date 4/11/2023
"""
import re

def check_id(input): 
    if(input.isdigit()):
        return True
    else:
        print("failed id check")
        return False
    print("failed id check")
def check_date(input): 
    date_pattern = "^^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$"
    match = re.match(date_pattern, input)
    if match: return True
    else:
        print("failed date check")
        return False