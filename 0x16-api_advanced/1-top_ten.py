#!/usr/bin/python3
"""
Queries the reddit Api
"""

import requests


def top_ten(subreddit):
    """
    Returns the titles a subreddit
    """

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
            "User-Agent": "Fake Agent"
            }
    response = requests.get(url, headers=headers)
    outcome = response.json()
    if response.status_code == 200:
        for sub in outcome['data']['children']:
            print(sub['data']['title'])
    else:
        print(None)
