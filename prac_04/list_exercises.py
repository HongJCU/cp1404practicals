
numbers = []


for i in range(5):
    num = float(input("Number: "))
    numbers.append(num)


for num in numbers:
    print(f"Number: {num}")


print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {sum(numbers) / len(numbers)}")