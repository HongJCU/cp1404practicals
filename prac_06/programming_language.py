"""CP1404/CP5632 Practical - Programming Language class."""

class ProgrammingLanguage:

#Definition of init with information fields
    def __init__(self,name, typing, reflection , year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

def is_dynamtic(self):
    # Check if the user inpput the languge name is dynamically typed or not
    return self.typing.lower() == "dynamic"

def __str__(self):
# Pulling the value from four different attributes of the object (self.name, self.typing, self.reflection, and self.year)
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
