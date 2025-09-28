def print_menu():
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")

name_user=input("Enter name: ")

print_menu()

user_choice=input(">>> ")

while user_choice != "Q":
    if user_choice == "H":
        print("Hello",name_user)
    elif user_choice == "G":
        print("Goodbye",name_user)
    else:
        print("Invalid choice")

    print_menu()
    user_choice=input(">>> ")

print("Finished.")
