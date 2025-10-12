"""
CP1404/CP5632 Practical
List comprehensions
"""

names = ["Bob", "Angel", "Jimi", "Alan", "Ada"]
full_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing", "Ada Lovelace"]

# for loop that creates a new list containing the first letter of each name
first_initials = []
for name in names:
    first_initials.append(name[0])
print(first_initials)

# list comprehension that does the same thing as the loop above
first_initials = [name[0] for name in names]
print(first_initials)

# list comprehension that creates a list containing the initials
full_initials = [name.split()[0][0] + name.split()[1][0] for name in full_names]
print(full_initials)

# filtering names that start with A
a_names = [name for name in names if name.startswith('A')]
print(a_names)

# join string method to create a single string from the names
print(" ".join(sorted(names)))

# TODOs completed below 👇
lowercase_full_names = [name.lower() for name in full_names]
print(lowercase_full_names)

almost_numbers = ['0', '10', '21', '3', '-7', '88', '9']
numbers = [int(num) for num in almost_numbers]
print(numbers)

greater_than_nine = [num for num in numbers if num > 9]
print(greater_than_nine)

long_name_lastnames = ", ".join([name.split()[1] for name in full_names if len(name) > 11])
print(long_name_lastnames)
