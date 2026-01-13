"""CP1404 Practical - My Guitars Program"""

from guitar import Guitar
import csv


def main():
    """Read guitars from file, display them, allow user to add more, then save."""
    guitars = load_guitars("guitars.csv")
    display_guitars(guitars, "Existing guitars:")

    # Add new guitars
    guitars = add_new_guitars(guitars)

    # Sort by year
    guitars.sort()
    display_guitars(guitars, "All guitars (sorted by year):")

    # Save updated list
    save_guitars("guitars.csv", guitars)
    print("Guitars have been saved to guitars.csv")


def load_guitars(filename):
    """Read guitars from a CSV file and return a list of Guitar objects."""
    guitars = []
    with open(filename, "r", newline='') as in_file:
        reader = csv.reader(in_file)
        for row in reader:
            name, year, cost = row
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def display_guitars(guitars, title):
    """Display a list of guitars with a title."""
    print(f"\n{title}")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar}{vintage_string}")


def add_new_guitars(guitars):
    """Prompt user to add new guitars and return updated list."""
    print("\nEnter your new guitars (or press Enter to stop):")
    while True:
        name = input("Name: ").strip()
        if not name:
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.")
    return guitars


def save_guitars(filename, guitars):
    """Save the list of Guitar objects to a CSV file."""
    with open(filename, "w", newline='') as out_file:
        writer = csv.writer(out_file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


if __name__ == "__main__":
    main()
