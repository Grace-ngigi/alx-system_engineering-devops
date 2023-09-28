#!/usr/bin/python3
"""
Dictionary of list of dictionaries
"""

import json
import requests


def list_todo_all_employees():
    """
    Records all tasks from all employees
    """
    base_url = "https://jsonplaceholder.typicode.com/"
    res = requests.get(base_url + "users").json()

    data = {}

    for user in res:
        user_id = user.get("id")
        user_todos = requests.get(base_url + "todos",
                                  params={"userId": user_id}).json()
        user_data = [
                {
                    "tasks": t.get("title"),
                    "completed": t.get("completed"),
                    "username": user.get("username")
                }
                for t in user_todos
            ]
        data[user_id] = user_data
    with open("todo_all_employees.json", "w") as file:
        json.dump(data, file)


if __name__ == "__main__":
    list_todo_all_employees()
