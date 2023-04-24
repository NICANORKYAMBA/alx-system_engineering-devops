#!/usr/bin/python3
"""
Python script that, uses REST API, for all employees,
returns information about their TODO list progress.
"""
import json
import requests
import sys


if __name__ == '__main__':
    BASE_URL = 'https://jsonplaceholder.typicode.com'

    """Make a GET request to retrieve all users"""
    response = requests.get('{}/users'.format(BASE_URL))
    users = response.json()

    """Create a dictionary to hold all tasks"""
    all_tasks = {}

    """Iterate over each employee ID"""
    for user in users:
        user_id = user['id']
        username = user['username']

        """Make a GET request to retrieve the employee's TODO list"""
        response = requests.get('{}/todos?userId={}'.format(
            BASE_URL, user_id))
        todos = response.json()

        """Add the tasks to the all_tasks dictionary"""
        user_tasks = []
        for todo in todos:
            task = {'username': username,
                    'task': todo['title'],
                    'completed': todo['completed']}
            user_tasks.append(task)

        all_tasks[user_id] = user_tasks

    """Save the all_tasks dictionary to a JSON file"""
    with open('todo_all_employees.json', 'w') as file:
        json.dump(all_tasks, file, indent=4)
