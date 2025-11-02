"""CP1404/CP5632 Practical - Programming Language class."""

class ProgrammingLanguage:

#Definition of init with information fields
    def __init__(self,name, typing, reflection , year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

def is_dynamtic(self):
    return self.typing.lower() == "dynamic"

