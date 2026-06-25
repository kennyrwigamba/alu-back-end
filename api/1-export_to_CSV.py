#!/usr/bin/python3
"""Export an employee's TODO list to CSV from a REST API."""

import csv
import json
from sys import argv
from urllib.request import urlopen


API_URL = "https://jsonplaceholder.typicode.com"


def main():
    """Write the employee's tasks to a CSV file named after the user ID."""
    employee_id = int(argv[1])

    with urlopen(f"{API_URL}/users/{employee_id}") as response:
        employee = json.load(response)

    with urlopen(f"{API_URL}/todos?userId={employee_id}") as response:
        tasks = json.load(response)

    with open(f"{employee_id}.csv", "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for task in tasks:
            writer.writerow(
                [
                    employee.get("id"),
                    employee.get("username"),
                    task.get("completed"),
                    task.get("title"),
                ]
            )


if __name__ == "__main__":
    main()