#importing regular expression library for matching 
import re
#defining the function  "email_validator"
def email_validator(mail):
    #assigning the a pattern for matching with original mail given by user
    pattern = r'^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-z]{2,}$'
    #returning with function re.match(pattern,value)
    return re.match(pattern,mail) is not None
#input by user 
mail= input("enter the email :")
#assigning a variable with function
result = email_validator(mail)
#conditions
if result:
    print("valid email")
else:
    print("Invalid email")

