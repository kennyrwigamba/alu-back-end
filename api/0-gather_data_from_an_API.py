#!/usr/bin/python3
"""Gather and display an employee's TODO list progress from an API."""

import json
from sys import argv
from urllib.request import urlopen


API_URL = "https://jsonplaceholder.typicode.com"


def main():
    """Print the completed tasks for the employee identified by argv."""
    employee_id = int(argv[1])

    with urlopen(f"{API_URL}/users/{employee_id}") as response:
        employee = json.load(response)

    with urlopen(f"{API_URL}/todos?userId={employee_id}") as response:
        tasks = json.load(response)

    completed_tasks = [task for task in tasks if task.get("completed")]

    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee.get("name"),
            len(completed_tasks),
            len(tasks),
        )
    )

    for task in completed_tasks:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    main()
