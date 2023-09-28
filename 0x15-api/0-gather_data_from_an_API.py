#!/usr/bin/python3
"""
Collects data from a given api and display it
"""
import json
import requests
import sys

employee_id = sys.argv[1]

# Define the base URL for the JSONPlaceholder API
base_url = 'https://jsonplaceholder.typicode.com/'

# Fetch user details
user_response = requests.get(f'{base_url}users/{employee_id}')
user_data = user_response.json()

# Fetch user's TODO list
todo_response = requests.get(f'{base_url}todos?userId={employee_id}')
todo_data = todo_response.json()

# Calculate the number of completed and total tasks
total_tasks = len(todo_data)
completed_tasks = sum(1 for task in todo_data if task['completed'])

# Display the employee's TODO list progress
print("Employee {} is done with tasks ({}/{}):"
      .format(user_data['name'], completed_tasks, total_tasks))

# Display the titles of completed tasks
print("Completed Tasks:")
for task in todo_data:
    if task['completed']:
        print(f"\t{task['title']}")
