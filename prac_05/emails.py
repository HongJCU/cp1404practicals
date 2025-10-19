"""
emails
Estimate: 20 minutes
Actual:   32 minutes
"""

#Added a function to split the email between . and @ to get the first and last name
def get_name_from_email(email):
    prefix = email.split("@")[0]
    parts =  prefix.split('.')
    name = "".join(parts).title()
    return name

emails = input("Enter emails separated by space: ")
print(emails)