#!/usr/bin/python3
"""
Contains the number_of_subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of total subscribers"""
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = "https://api.reddit.com/r/{}/about".format(subreddit)
    headers = {'User-Agent': 'CustomClient/1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    try:
        data = response.json().get('data')
        if data:
            return data.get('subscribers', 0)
        return 0
    except ValueError:
        return 0
