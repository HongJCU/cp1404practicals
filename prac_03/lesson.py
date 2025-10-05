# Write a program read adn print if file has # in it, user enter file name
"""
FILENAME = input("Enter filename: ")
in_file = open(FILENAME, "r")
for line in in_file:
    if line.startswith("#"):
        print(line.rstrip())
in_file.close()"""

#### Lesson 2 : read a text string
"""s= "\tPython, Monty  \n"
print(s)
# print(len(s))
print(s[1],".",sep=" ")
print(s.strip(),".",sep=" ")
s = s.replace(' ','*')
print(s)
# print(s.lstrip(),".",sep="")
# print(s.strip().split(','))
#
# print(list(s))"""

"""# rewrite tge following code
name = input("Name: ")
out_file = open("name.txt", "w")
print(name,file=out_file)
out_file.close()
print("Done")"""

"""name = input("Name: ")
with open("name.txt", "w") as out_file:
    print(name,file= out_file)
    print("Done")"""

# write code that creates files from a list of strings. Each file should be named with the value of the string a .txt extension.
# If the string is "Bob", create a file called "Bob.txt". Write the string to the file
"""
name = input("Name: ")
with open("name.txt", "w") as out_file:
    for name in out_file:
        print(name,file=out_file)
        print("Done")"""

### names=["Cliff","Lukas","lea"]
# for i in range(len(names)):
# with open(f"{names[i]}.txt","w") as out_file:
# print ( f"{names[i]}.", file=out_file)

# write code to read a file like this and print each data pair, like "Bob was born in NZ"
#Bob \n
#NZ\n
#Jane\n
#Myanmar \n
#Derek \n
#Australia \n
"""
data_user=["Bob\n","NZ\n","Jane\n","Myanmar\n","Derek\n","Austrailia\n"]
for user in data_user:
    print(user)
    """
'''you need to read a txt file not create a list '''

""""""


with open("name.txt") as in_file:
    lines = in_file.readlines()

print(lines)

for i in range(0,len(lines),2):
    name = lines[i].strip()
    country = lines[i+1].strip()
    print(f"{name} is live at {country}")


"""# Complete this code ( pract question )
is_finished = False
while not is_finished:
    try:
        result=int(input("Enter a valid integer: "))
        is_finished = True
    except ValueError:
        print("Enter a valid integer")
    else:
        print(f"NExt year you will be {age +1}")
    finally:
        print("Good try")
        """

"only string have index number but not the interger"