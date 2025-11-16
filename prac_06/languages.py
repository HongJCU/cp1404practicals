
"""CP1404/CP5632 Practical - Programming Language class."""



"""CP1404/CP5632 Practical - Langugage class example."""
"""
car
Estimate: 30 minutes
Actual:   45 minutes
"""


from programming_language import ProgrammingLanguage

def main():
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [python, ruby, visual_basic]

    for language in languages:
        print(language)

    print("\nThe dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)

main()
