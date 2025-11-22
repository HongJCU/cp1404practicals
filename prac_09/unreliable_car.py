import random
from prac_09.car import Car

class UnreliableCar(Car):

    def __init__(self, name="", fuel=0, reliability=100.0):
        """Initialise an UnreliableCar with a reliability percentage."""
        super().__init__(name, fuel)
        self.reliability = float(reliability)

    def drive(self, distance):
        """Attempt to drive; succeed only if random roll is < reliability"""
        roll = random.uniform(0, 100)
        if roll < self.reliability:
            return super().drive(distance)
        # Failed to drive this attempt
        return 0