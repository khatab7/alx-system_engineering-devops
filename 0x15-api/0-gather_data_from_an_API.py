#!/usr/bin/python3
"""
A Script that, uses this REST API, for a given employee ID, returns
information about his/her TODO list progress
"""

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    emp_id = sys.argv[1]
    user_res = requests.get(url + "users/{}".format(emp_id))
    user = user_res.json()
    params = {"userId": emp_id}
    todos_res = requests.get(url + "todos", params=params)
    todos = todos_res.json()
    completed = []
    for todo in todos:
        if todo.get("completed") is True:
            completed.append(todo.get("title"))
    name = user.get("name")
    compi = len(completed)
    lentodo = len(todos)
    print("Employee {} is done with tasks({}/{})".format(name, compi, lentodo))
    for complete in completed:
        print("\t {}".format(complete))
