class User:
    def __init__(self, name):
        self.name = name
        self.tacos = 5
        self.score = 0

    def give_taco(self, other_user):
        """Give a taco to another user, reducing your count and increasing their score."""
        if self.tacos > 0:
            self.tacos -= 1
            other_user.score += 1
            print(f"{self.name} gave a taco to {other_user.name} 🌮")
        else:
            print(f"{self.name} has no tacos left to give!")

    def __str__(self):
        """Return a nice printable version of the user."""
        return f"{self.name}, {self.score} points, {self.tacos} tacos left"

# Create some users
ben = User("Ben")
maya = User("Maya")

# Ben gives a taco to Maya
ben.give_taco(maya)

# Print both users
print(ben)   # Ben, 0 points, 4 tacos left
print(maya)  # Maya, 1 points, 5 tacos left
