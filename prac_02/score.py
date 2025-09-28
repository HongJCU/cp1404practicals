"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random
def main():

    score = float(input("Enter score: "))
    result = result_condition(score)
    print(f"Your score is: {score}, Your result is: {result}")

    random_score = random.randint(0, 100)
    print(f"Random score:' {random_score}, This result is {result_condition(random_score)}")


def result_condition(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()
