#!/usr/bin/python3

import requests
from sys import argv

username = argv[1]

url =  f"https://www.reddit.com/user/{username}/about.json"
headers = {
        "User-Agent": "Fake Agent"
        }

response = requests.get(url, headers=headers)
if response.status_code == 200:
    data = response.json()
    print(f"User information: {data}")
    print(data['kind'])
else:
    print("Request failed with status code:", response.status_code)
