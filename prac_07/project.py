"""CP1404 Practical - Project class
Estimate: 60 minutes
Actual:   80 minutes
"""

from datetime import date


class Project:
    """Represent a project with name, start date, priority, cost estimate, and completion percentage."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialise a Project."""
        self.name = name
        self.start_date = start_date  # a datetime.date object
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

   
