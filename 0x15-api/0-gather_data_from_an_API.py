#!/usr/bin/python3
"""
Collects data from a given api and display it
"""

from collections import Counter
import json
import requests
import sys


def fetch_todos(user_id):
    url = "https://jsonplaceholder.typicode.com/"

    todos_res = requests.get(url + "todos?userId=" + user_id)
    user_res = requests.get(url + "users/" + user_id).json()

    if todos_res.status_code == 200:
        todos = todos_res.json()

    completed_tasks = [task for task in todos if task['completed']]
    print("Employee {} is done with tasks({}/{}):"
          .format(user_res.get("name"), len(completed_tasks), len(todos)))
    for task in completed_tasks:
        print("\t{}".format(task.get("title")))


if __name__ == "__main__":
    fetch_todos(sys.argv[1])
