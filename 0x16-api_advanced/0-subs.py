#!/usr/bin/python3
"""
 a function that queries the Reddit API and returns the number
 of subscribers (not active users, total subscribers)
 for a given subreddit. If an invalid subreddit is given,
 the function should return 0.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Gets the number of subscribers of a subreddit
    if not a valid subreddit, return 0.
    """

    url = f"\
            https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
            "User-Agent": "Fake Agent"
            }
    response = requests.get(url, headers=headers)
    outcome = response.json()
    if response.status_code != 200:
        data = 0
    else:
        data = outcome.get('data').get('subscribers')
    return data
