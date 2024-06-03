#!/usr/bin/python3
"""
Using the REST API for a given employee ID, returns
information about their TODO list progress
"""

import requests
import sys

if __name__ == "__main__":
    # Get the user ID from the command line arguments
    userId = sys.argv[1]
    # Request user data from the API
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId))
    # Extract the user's name from the response
    name = user.json().get('name')
    # Request TODO list data from the API
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    totalTasks = 0
    completed = 0

    # Iterate over each task in the TODO list
    for task in todos.json():
        # Check if the task belongs to the given user
        if task.get('userId') == int(userId):
            totalTasks += 1  # Increment the total task count
            if task.get('completed'):
                completed += 1

    # Print the summary of tasks
    print('Employee {} is done with tasks({}/{}):'
          .format(name, completed, totalTasks))

    # Print the titles of completed tasks
    print('\n'.join(["\t " + task.get('title') for task in todos.json()
          if task.get('userId') == int(userId) and task.get('completed')]))
