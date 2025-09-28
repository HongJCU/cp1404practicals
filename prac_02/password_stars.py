
"""Module docstring"""


# imports
# CONSTANTS

def main():
    password_user = get_password()
    convert_password(password_user)


def convert_password(password_user: str):
    asterisk_string = "*" * len(password_user)
    print(asterisk_string)


def get_password() -> str:
    password_user = input("Please enter your password: ")

    while len(password_user) < 3:
        print("Password is too short")
        password_user = input("Please enter your password: ")
    return password_user


main()