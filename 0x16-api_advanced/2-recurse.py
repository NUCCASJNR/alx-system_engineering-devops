#!/usr/bin/python3
"""Queries the Reddit API and returns a list
 containing the titles of all hot"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Returns a list containing the titles of all
      hot articles for a subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    if hot_list == []:
        hot_list = []
    headers = {
            "User-Agent": "Fake Agent"
            }
    params = {'after': after} if after else {}
    response = requests.get(url, headers=headers, params=params)
    outcome = response.json()
    if response.status_code == 200:
        for sub in outcome['data']['children']:
            hot_list.append(sub['data']['title'])
        after = outcome['data']['after']
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
