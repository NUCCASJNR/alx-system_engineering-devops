#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python
script to export data in the JSON format.

Requirements:

Records all tasks that are owned by this employee
Format must be: { "USER_ID": [{"task": "TASK_TITLE", "completed":
TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task":
"TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
"username": "USERNAME"}, ... ]}
File name must be: USER_ID.json

"""

import json
import requests
import sys

if __name__ == "__main__":
    emp_id = sys.argv[1]
    url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    res = requests.get(url)
    new_url = url + "/todos"
    new_res = requests.get(new_url)
    if new_res.status_code == 200:
        data = res.json()
        name = data.get('name')
        tasks = new_res.json()

        file = f"{emp_id}.json"
        with open(file, "w") as json_file:
            for task in tasks:
                user_id = task.get("userId")
                completed = task.get("completed")
                title = task.get("title")
                task_object = {
                        user_id: [{
                            "task": title,
                            "completed": completed,
                            "username": name}]
                        }
            json.dump(task_object, json_file)
    else:
        print(f"Error: {new_res.status_code}")
