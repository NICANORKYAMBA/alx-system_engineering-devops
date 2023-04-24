#!/usr/bin/python3
"""
Python script that, uses REST API, for a given
employee ID, returns information about his/her
TODO list progress.
Exports data in the CSV format.
"""
import csv
import requests
import sys


if __name__ == '__main__':
    BASE_URL = 'https://jsonplaceholder.typicode.com/'

    """Get the employee ID from the command-line arguments"""
    if len(sys.argv) < 2:
        print("Please provide an employee ID as an argument")
        sys.exit(1)
    employee_id = int(sys.argv[1])

    """Make a GET request to retrieve the employee's TODO list"""
    response = requests.get(
            BASE_URL + "users/{}".format(employee_id)).json()

    """Get employee name from API"""
    employee_name = response.get("username")
    todos = requests.get(
            BASE_URL + "todos", params={"userId": employee_id}).json()

    """Export data to CSV"""
    csv_filename = '{}.csv'.format(employee_id)
    with open(csv_filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow(
                    [employee_id, employee_name,
                        todo['completed'], todo['title']])
