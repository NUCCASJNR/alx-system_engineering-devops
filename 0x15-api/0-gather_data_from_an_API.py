#!/usr/bin/python3
"""
Python script that, using this REST API, for a given
employee ID, returns information about his/her TODO list progress.

Requirements:

You must use urllib or requests module
The script must accept an integer as a parameter, which is
the employee ID
The script must display on the standard output
the employee TODO list progress in this exact format:
First line: Employee EMPLOYEE_NAME is done with
tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
EMPLOYEE_NAME: name of the employee
NUMBER_OF_DONE_TASKS: number of completed tasks
TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the
sum of completed and non-completed tasks
Second and N next lines display the title of completed tasks:
TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)
"""

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
        name = f"{data.get('name')}"
        tasks = new_res.json()
        # print(tasks)
        real = []
        for i in tasks:
            if i.get("completed") is True:
                real.append(i)
        # print(real)
        titles = []
        for task in tasks:
            if task.get("completed") is True:
                titles.append(task.get("title"))
        done = f"Employee {name} is done with tasks"
        print("{} {}/{}:".format(done, len(real), len(tasks)))
        for tit in titles:
            print("\t {}".format(tit))
    else:
        print(f"Error: {res.status_code}")
