"""names = ["Ada", "Alan"]
print(", ".join(names))
name_to_remove=input("Who do you want to remove? ").title()

while name_to_remove !="":
    name_to_remove=input("Who do you want to remove? ").title()
    try:
        names.remove(name_to_remove)
    except ValueError:
        print("Name not found")
    print(names)
    name_to_remove=input("Who do you want to remove? ").title()

print("Good Try")

# function names.remove and join(names)"""

data = [['Derek',7],['Xavier',80],['Bob',612],['Chantanelle',9]]
for pair in data:
    print(pair[0],pair[1])
    print(pair)


# Desired out put from any similar list of[name,score] pairs:
#Derek -7
#Xavier = 80
# Bob =612
# Chantanelle = 9

