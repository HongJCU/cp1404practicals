"""
Loop-based tests for UnreliableCar.
CP1404/CP5632 Practical
"""

import random
from prac_09.unreliable_car import UnreliableCar

def main():
    random.seed(42)

    print("Testing UnreliableCar with loop-based tests\n")
    print("Testing 0% reliability (should never drive):")
    car = UnreliableCar("Barely Works", fuel=50, reliability=0)

    attempts = 20
    successes = 0
    for _ in range(attempts):
        if car.drive(1) > 0:
            successes += 1

    print(f"  Attempts: {attempts}, Successful drives: {successes}")
    print(f"  Expected: 0\n")

    print("Testing 100% reliability (should always drive):")
    car = UnreliableCar("Always Works", fuel=20, reliability=100)

    attempts = 20
    successes = 0
    for _ in range(attempts):
        if car.drive(1) > 0:
            successes += 1

    print(f"  Attempts: {attempts}, Successful drives: {successes}")
    print(f"  Expected: {attempts}\n")
    print("Testing 30% reliability statistically:")

    reliability = 30
    attempts = 1000
    car = UnreliableCar("Kinda Works", fuel=attempts, reliability=reliability)

    successes = 0
    for _ in range(attempts):
        if car.drive(1) > 0:
            successes += 1

    observed = successes / attempts * 100

    print(f"  Attempts: {attempts}")
    print(f"  Expected approx reliability: {reliability}%")
    print(f"  Observed success rate: {observed:.1f}%")
    print("  (If it's far from expected, something is wrong!)\n")

if __name__ == "__main__":
    main()
