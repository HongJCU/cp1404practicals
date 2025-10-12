"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():

    subject_records = load_data(FILENAME)
    display_subject_details(subject_records)


def load_data(filename=FILENAME):

    subject_records = []
    input_file = open(filename)
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        subject_records.append(parts)
    input_file.close()
    return subject_records


def display_subject_details(subject_records):

    for subject_code, lecturer, num_students in subject_records:
        print(f"{subject_code} is taught by {lecturer} and has {num_students} students")


main()
