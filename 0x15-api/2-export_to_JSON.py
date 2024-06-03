#!/usr/bin/python3
"""Exports data in the JSON format"""

if __name__ == "__main__":

    import json
    import requests
    import sys

    # Get the user ID from the command line arguments
    userId = sys.argv[1]

    # Request user data from the API
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId))
    # Request TODO list data from the API
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()

    # Dictionary to store user's TODO list information
    todoUser = {}
    taskList = []

    # Iterate over each task in the TODO list
    for task in todos:
        # Check if the task belongs to the given user
        if task.get('userId') == int(userId):
            # Create a dictionary for the task details
            taskDict = {"task": task.get('title'),
                        "completed": task.get('completed'),
                        "username": user.json().get('username')}
            # Append the task dictionary to the task list
            taskList.append(taskDict)
    # Add the task list to the user's data in the dictionary
    todoUser[userId] = taskList

    # Define the filename for the JSON file
    filename = userId + '.json'
    # Write the user's TODO list data to the JSON file
    with open(filename, mode='w') as f:
        json.dump(todoUser, f)
