#!/usr/bin/python3

import requests
import sys

user = sys.argv[1]
#url = f"https://api.github.com/users/{user}"
url = f"https://jsonplaceholder.typicode.com/todos/{user}"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(f"{data.get('id')}")
else:
    print('Error:', response.status_code)
