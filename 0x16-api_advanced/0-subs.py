#!/usr/bin/python3
"""
Queries the reddit Api
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers of a subreddit
    """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
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
