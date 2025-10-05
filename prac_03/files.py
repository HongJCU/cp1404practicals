# 1. Ask the user for their name and write it to "name.txt"
# Using open() and close()

name = input("Enter your name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# 2. Read the name from "name.txt" and print a greeting
# Using open() and close()

in_file = open("name.txt", "r")
name = in_file.read().strip()  # remove any newline characters
in_file.close()

print(f"Hi {name}!")

# 3. Read the first two numbers from "numbers.txt", add them and print the result
# Using with ... as ... (context manager) and readline()

with open("numbers.txt", "r") as in_file:
    first_number = int(in_file.readline())
    second_number = int(in_file.readline())
    result = first_number + second_number

print(result)

# 4. Print the total for *all* numbers in "numbers.txt"
# Using with ... as ... and for line in file
total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        number = int(line)
        total += number

print(total)