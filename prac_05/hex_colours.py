"""
CP1404/CP5632 Practical
Hex Color in dictionary
Reformatted to follow PEP 8 conventions
"""
# Adding color listing
COLOR_TO_CODE = {"Absolute Zero": "#0048ba","Acid Green": "#b0bf1a","Alice Blue": "#f0f8ff","Alizarin Crimson": "#e32636",
                 "Amethyst": "#9966cc","Amber": "#ffbf00","Apricot": "#fbceb1","Baby Pink": "#f4c2c2",
                 "Banana Yellow": "#ffe135","Bitter Lime": "#bfff00"}

# Print all color names and their codes neatly lined up
for color, code in COLOR_TO_CODE.items():
    print(f"{color:20} is {code}")

# Get user input and make it case-insensitive
color_name = input("Enter the color name: ").title()
while color_name != "":
    try:
        print(f"{color_name} is {COLOR_TO_CODE[color_name]}")
    except KeyError:
        print("Invalid color name")
    color_name = input("Enter the color name: ").title()