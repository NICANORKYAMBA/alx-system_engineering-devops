#!/usr/bin/python3
"""
Python script that uses REST API, for a given
employee ID, returns information about his/her TODO
list progress and exports data in the JSON format.
"""
import json
import requests
import sys

if __name__ == '__main__':

    BASE_URL = 'https://jsonplaceholder.typicode.com'

    """Get the employee ID from the command-line arguments"""
    if len(sys.argv) < 2:
        print('Please provide an employee ID as an argument.')
        sys.exit(1)

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
    employee_name = employee['username']

    """Create a dictionary with task information"""
    tasks = []
    for todo in todos:
        task = {}
        task['task'] = todo['title']
        task['completed'] = todo['completed']
        task['username'] = employee_name
        tasks.append(task)

    """Create a dictionary with user ID and task information"""
    user_tasks = {}
    user_tasks[str(user_id)] = tasks

    """Export data to JSON file"""
    filename = '{}.json'.format(user_id)
    with open(filename, 'w') as f:
        json.dump(user_tasks, f)
