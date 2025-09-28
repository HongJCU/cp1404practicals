import random

def main():

    num_scores = int(input("Enter a number of scores to generate: "))

    with open("results.txt", "w") as file:
        for _ in range(num_scores):
            score = random.randint(0, 100)
            result = result_condition(score)
            file.write(f"{score} is {result}\n")

    print(f"Generated {num_scores} random scores and saved results to results.txt")


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