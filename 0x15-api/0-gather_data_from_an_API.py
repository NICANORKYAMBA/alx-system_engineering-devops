#!/usr/bin/python3
"""
Python script that, uses REST API, for a given
employee ID, returns information about his/her TODO
list progress.
"""
import requests
import sys


BASE_URL = 'https://jsonplaceholder.typicode.com'
employee_id = int(sys.argv[1])

"""Make a GET request to retrieve the employee's TODO list"""
response = requests.get('{}/todos?userId={}'.format(
    BASE_URL, employee_id))

"""Parse the JSON response into a Python list of dictionaries"""
todos = response.json()

"""Calculate the number of completed and total tasks"""
total_tasks = len(todos)

completed_tasks = sum(1 for todo in todos if todo['completed'])

"""Get employee name from API"""
user_id = todos[0]['userId']
response = requests.get('{}/users/{}'.format(BASE_URL, user_id))
employee = response.json()
employee_name = employee['name']

"""Display the progress information"""
print("Employee {} is done with tasks({}/{}):".format(
    employee_name, completed_tasks, total_tasks))

"""Display the titles of completed tasks"""
for todo in todos:
    if todo['completed']:
        print('\t{}'.format(todo['title']))
