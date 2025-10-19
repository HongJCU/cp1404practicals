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

#Create a variable to transform from email to name
email_to_name = {}

# A loop to ask user to input the email address and confirm whethere is it correct or not 
email = input("Email: ")
while email != "":
    email_to_name[get_name_from_email(email)] = email
    name = get_name_from_email(email)
    confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()
    if confirmation not in("","y"):
        name = input("Name: ").title()
    email_to_name[email] = name
    email = input("Email: ")

emails = input("Enter emails separated by space: ")
print(emails)