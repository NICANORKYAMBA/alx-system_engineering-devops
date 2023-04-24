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
    BASE_URL = 'https://jsonplaceholder.typicode.com'

    """Get the employee ID from the command-line arguments"""
    if len(sys.argv) < 2:
        print("Please provide an employee ID as an argument")
        sys.exit(1)
    employee_id = int(sys.argv[1])

    """Make a GET request to retrieve the employee's TODO list"""
    response = requests.get("{}/todos?userId={}".format(
        BASE_URL, employee_id))

    """Parse the JSON response into a Python list of directories"""
    todos = response.json()

    """Get employee name from API"""
    response = requests.get("{}/users/{}".format(
        BASE_URL, employee_id))
    employee = response.json()
    employee_name = employee['name']

    """Export data to CSV"""
    csv_filename = '{}.csv'.format(employee_id)
    with open(csv_filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for todo in todos:
            writer.writerow(
                    [employee_id, employee_name,
                        todo['completed'], todo['title']])
