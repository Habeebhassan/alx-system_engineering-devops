#!/usr/bin/python3
"""
Contains the number_of_subscriber
"""

import requests
import logging

def number_of_subscribers(subreddit):
    """returns the number of total subscribers"""
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = f"https://api.reddit.com/r/{subreddit}/about"
    headers = {'User-Agent': 'CustomClient/1.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

        data = response.json().get('data')
        if data:
            return data.get('subscribers', 0)
        return 0

    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}")
        return 0
    except ValueError as e:
        logging.error(f"Failed to parse JSON: {e}")
        return 0

