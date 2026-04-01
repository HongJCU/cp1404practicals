"""Band class for CP1404 - A band that has Musicians."""
from typing import List
from musician import Musician


class Band:
    def __init__(self, name: str = ""):
        """Initialise a Band with a name and empty list of musicians."""
        self.name = name
        self.musicians: List[Musician] = []

    def add(self, musician: Musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def __str__(self):
        """Return a string representation of the band and its musicians."""
        members = ", ".join(str(m) for m in self.musicians)
        return f"{self.name} ({members})"

    def __repr__(self):
        """Return a representation of the band showing its variables."""
        return str(vars(self))

    def play(self):
        """Return performance lines for each musician."""
        return "\n".join(m.play() for m in self.musicians)
