"""
Program to calculate and display a user's total price for a number of items, each with different prices.
If the total price is over $100, then a 10% discount is applied

"""
total_price = 0.0
price_of_items = 0.0
number_of_items=int(input("Number of items: "))
while number_of_items <= 0:
    print("Invalid number of items!")

    number_of_items = int(input("Number of items: "))

for i in range(1, number_of_items + 1):
        price_of_items = float(input(f"Price of item: "))
        total_price+=price_of_items

if total_price > 100.0:
            total_price=total_price * 0.9

print(f"Total price for {number_of_items} items is ${total_price:.2f}")

