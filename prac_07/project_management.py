"""CP1404 Practical - Project Management Program
Estimate: 90 minutes
Actual:   100 minutes
"""

from datetime import datetime
from project import Project

FILENAME = "projects.txt"

def main():
    """Manage a list of projects loaded from a file."""
    print("Welcome to Pythonic Project Management")

    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")

    MENU = ("- (L)oad projects\n" "- (S)ave projects\n" "- (D)isplay projects\n" "- (F)ilter projects by date\n" "- (A)dd new project\n" "- (U)pdate project\n" "- (Q)uit")
    choice = ""
    while choice != "Q":
        print(MENU)
        choice = input(">>> ").strip().upper()
        if choice == "L":
            filename = input("Filename to load from: ").strip()
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")
        elif choice == "S":
            filename = input("Filename to save to: ").strip()
            save_projects(filename, projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects_by_date(projects)
        elif choice == "A":
            add_new_project(projects)
        elif choice == "U":
            update_project(projects)
        elif choice == "Q":
            confirm = input(f"Would you like to save to {FILENAME}? ").lower()
            if confirm.startswith("y"):
                save_projects(FILENAME, projects)
                print("Projects saved.")
            print("Thank you for using custom-built project management software")
        else:
            print("Invalid menu choice")

def load_projects(filename):
    """Load projects from a tab-delimited file into a list of Project objects."""
    projects = []
    with open(filename, "r") as in_file:
        in_file.readline()  # skip header
        for line in in_file:
            parts = line.strip().split('\t')
            if len(parts) < 5:
                continue
            name, start_date_str, priority, cost_estimate, completion_percentage = parts
            start_date = datetime.strptime(start_date_str, "%d/%m/%Y").date()
            project = Project(name, start_date, int(priority), float(cost_estimate), int(completion_percentage))
            projects.append(project)
    return projects

def save_projects(filename, projects):
    """Save the list of projects to a tab-delimited file."""
    with open(filename, "w") as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            print(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t"
                  f"{project.cost_estimate}\t{project.completion_percentage}", file=out_file)
    print(f"Projects saved to {filename}")

def display_projects(projects):
    """Display incomplete and completed projects, both sorted by priority."""
    incomplete = sorted([p for p in projects if not p.is_complete()])
    complete = sorted([p for p in projects if p.is_complete()])

    print("Incomplete projects:")
    for project in incomplete:
        print(f"  {project}")
    print("Completed projects:")
    for project in complete:
        print(f"  {project}")

def filter_projects_by_date(projects):
    """Ask for a date and display projects starting after that date."""
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    try:
        filter_date = datetime.strptime(date_string, "%d/%m/%Y").date()
    except ValueError:
        print("Invalid date format")
        return
    filtered = [p for p in projects if p.start_date >= filter_date]
    filtered.sort(key=lambda p: p.start_date)
    for project in filtered:
        print(project)

