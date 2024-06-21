#!/usr/bin/python3
"""
Contains the number_of_subscriber
"""


from requests import get


def number_of_subscribers(subreddit):
    """
    function which query the Reddit API and returns 
    the number of subscriber  for a given subreddit.
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Google Chrome Version 80.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=user_agent)
    results = response.json()

    try:
        return results.get('data').get('subscribers')

    except Exception:
        return 0
