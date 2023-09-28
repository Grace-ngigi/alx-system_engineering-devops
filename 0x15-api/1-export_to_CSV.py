#!/usr/bin/python3
"""
Exports Data in CSV format
"""
import csv
import requests
import sys


def create_user_csv(employee_id):
    base_url = "https://jsonplaceholder.typicode.com/"
    res = requests.get(base_url + "users/{}".format(employee_id)).json()
    todos = requests.get(base_url + "todos",
                         params={"userId": employee_id}).json()
    username = res.get("username")
    with open("{}.csv".format(employee_id), "w", newline="") as file:
        csv_writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        [csv_writer.writerow(
         [employee_id, username, t.get("completed"),
          t.get("title")]) for t in todos]


if __name__ == "__main__":
    employee_id = sys.argv[1]
    create_user_csv(employee_id)
