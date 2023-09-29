#!/usr/bin/python3
"""
Export to json
"""

import json
import requests
import sys


def create_json_file(employee_id):
    """
Create a json file with all tasks from all employees
    """
    base_url = "https://jsonplaceholder.typicode.com/"
    res = requests.get(base_url + "users/{}".format(employee_id)).json()
    todos = requests.get(base_url + "todos",
                         params={"userId": employee_id}).json()
    username = res.get("username")
    data = {
            employee_id: []
            }
    for task in todos:
        tasks = {
                "task": task["title"],
                "completed": task["completed"],
                "username": username
                }
        data[employee_id].append(tasks)
    with open("{}.json".format(employee_id), "w") as file:
        json.dump(data, file)


if __name__ == "__main__":
    user_id = sys.argv[1]
    create_json_file(user_id)
