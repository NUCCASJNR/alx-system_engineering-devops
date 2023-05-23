#!/usr/bin/python3

"""
Gathers information from an Api
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
        print("{}({}/{}):".format(done, len(real), len(tasks)))
        for tit in titles:
            print("\t {}".format(tit))
    else:
        print(f"Error: {res.status_code}")
