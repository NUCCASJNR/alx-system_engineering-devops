#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python
script to export data in the CSV format.

Requirements:

Records all tasks that are owned by this employee
Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS",
"TASK_TITLE"
File name must be: USER_ID.csv
"""

import csv
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
        tasks = new_res.json()
        name = f"{data.get('username')}"

        file_name = f"{emp_id}.csv"
        with open(file_name, "w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            for task in tasks:
                user_id = task.get('userId')
                completed = task.get('completed')
                title = task.get('title')
                writer.writerow([user_id, name, completed, title])
    else:
        print(f"Error: {new_res.status_code}")
