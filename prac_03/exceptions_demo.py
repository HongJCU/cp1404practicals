"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
1. Will only occur if user input/ type in not a number

2. When will a ZeroDivisionError occur?
2. Will only occur if user input/type in zero for denominator

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
3. Yes by adding a while loop to check and change the input 
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
    while denominator == 0:
        denominator = int(input("Enter the denominator: "))

fraction = numerator / denominator
print(fraction)
print("Finished.")