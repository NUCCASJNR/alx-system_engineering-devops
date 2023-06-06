#!/usr/bin/python3

import requests
from sys import argv

reddit = argv[1]

url =  f"https://www.reddit.com/r/{reddit}/about.json"
headers = {
        "User-Agent": "Fake Agent"
        }

response = requests.get(url, headers=headers)
if response.status_code == 200:
    data = response.json()
#   print(f"User information: {data}")
    print(data['data']['subscribers'])
else:
    print("Request failed with status code:", response.status_code)
