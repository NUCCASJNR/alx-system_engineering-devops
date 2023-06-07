#!/usr/bin/python3
"""Queries the Reddit API and returns a list
 containing the titles of all hot"""

import requests


def recurse(subreddit, hot_list=[]):
    """Returns a list containing the titles of all hot articles for a subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
            "User-Agent": "Fake Agent"
            }
    response = requests.get(url, headers=headers)
    outcome = response.json()
    if response.status_code == 200:
        for sub in outcome['data']['children']:
            hot_list.append(sub['data']['title'])
        if outcome['data']['after'] is not None:
            return recurse(subreddit, hot_list)
        else:
            return hot_list
    else:
        return None