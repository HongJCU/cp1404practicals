"""CP1404 Practical - guitars program"""
"""
Estimate: 45 minutes
Actual:   2 hours 30 minutes
"""
from guitar import Guitar

def main():
    """Get guitar details and store them in a list, then display the list."""
    guitars = []

    print("My guitars!")
    name = input("Name: ")
    while name != "":
        try:
            year = int(input("Year: "))
            cost = float(input("Cost: $"))
            guitar_to_add = Guitar(name, year, cost)
            guitars.append(guitar_to_add)
            print(f"{guitar_to_add.name} ({guitar_to_add.year}) : ${guitar_to_add.cost:,.2f} added.")
        except ValueError:
            print("Invalid input. Please enter a valid number for year and cost.")
        name = input("Name: ")

    if not guitars:
        print("No guitars added.")
    else:
        guitars.sort()
        print("\nThese are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = " (vintage)"
            print(f"Guitar {i}: {guitar.name} ({guitar.year}), worth ${guitar.cost:,.2f}{vintage_string}")

    main()

