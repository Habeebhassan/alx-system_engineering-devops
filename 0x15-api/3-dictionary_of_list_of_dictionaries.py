#!/usr/bin/python3
"""Exports data in the JSON format"""

if __name__ == "__main__":

    import json  # Importing the json module for handling JSON data
    import requests  # Importing the requests module for making HTTP requests
    import sys  # Importing the sys module for system-specific

    # Making a GET request to fetch user data from the JSONPlaceholder API
    users = requests.get("https://jsonplaceholder.typicode.com/users")
    # Converting the JSON response to a Python dictionary
    users = users.json()

    # Making a GET request to fetch task data from the JSONPlaceholder API
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    # Converting the JSON response to a Python dictionary
    todos = todos.json()

    # Initializing an empty dictionary to store tasks for each user
    todoAll = {}

    # Iterating over each user
    for user in users:
        # Initializing an empty list to store tasks for the current user
        taskList = []
        # Iterating over each task
        for task in todos:
            # Checking if the current task belongs to the current user
            if task.get('userId') == user.get('id'):
                # Creating a dictionary to represent the task
                taskDict = {
                    "username": user.get('username'),
                    "task": task.get('title'),
                    "completed": task.get('completed')
                }
                # Adding the task dictionary to the task
                taskList.append(taskDict)
        # Adding the task list for the current user to the todoAll dictionary
        todoAll[user.get('id')] = taskList

    # Writing the todoAll dictionary to a JSON file'
    with open('todo_all_employees.json', mode='w') as f:
        json.dump(todoAll, f)
