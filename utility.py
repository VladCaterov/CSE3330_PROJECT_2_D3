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
    date_pattern = "^\d{4}-\d{2}-\d{2}$"
    match = re.match(date_pattern, input)
    if match: return True
    else:
        print("failed date check")
        return False
def check_string(input):
    if(isinstance(input, str)):
        return True
    else:
        print("failed string check")
        return False
def check_phone(input):
    phone_pattern = "^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$"
    match = re.match(phone_pattern, input)
    if match: return True
    else:
        print("failed phone check")
        return False
