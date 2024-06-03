#!/usr/bin/python3
"""Exports data in the CSV format"""

if __name__ == "__main__":

    import csv
    import requests
    import sys

    # Get the user ID from the command line arguments
    userId = sys.argv[1]
    # Request user data from the API
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId))
    # Extract the user's username from the response
    name = user.json().get('username')
    # Request TODO list data from the API
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    # Define the filename for the CSV file
    filename = userId + '.csv'
    
    # Open the CSV file for writing
    with open(filename, mode='w') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL, lineterminator='\n')
        # Iterate over each task in the TODO list
        for task in todos.json():
            # Check if the task belongs to the given user
            if task.get('userId') == int(userId):
                # Write the task data to the CSV file
                writer.writerow([userId, name, str(task.get('completed')),
                                 task.get('title')])
