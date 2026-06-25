#!/usr/bin/python3
"""Export an employee's TODO list to JSON from a REST API."""

import json
from sys import argv
from urllib.request import urlopen


API_URL = "https://jsonplaceholder.typicode.com"


def main():
    """Write the employee's tasks to a JSON file named after the user ID."""
    employee_id = int(argv[1])

    with urlopen(f"{API_URL}/users/{employee_id}") as response:
        employee = json.load(response)

    with urlopen(f"{API_URL}/todos?userId={employee_id}") as response:
        tasks = json.load(response)

    output = {
        str(employee.get("id")): [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": employee.get("username"),
            }
            for task in tasks
        ]
    }

    with open(f"{employee_id}.json", "w", encoding="utf-8") as json_file:
        json.dump(output, json_file)


if __name__ == "__main__":
    main()