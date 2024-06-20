#!/usr/bin/python3
""" Module to query the Reddit API recursively and count specific words in hot article titles. """

import requests

def count_words(subreddit, word_list, after='', word_dict={}):
    """
    Recursively queries the Reddit API to parse titles of hot articles and count specified keywords.

    The function prints a sorted count of the given keywords (case-insensitive).
    For example, 'Javascript' should be counted as 'javascript', but 'java' should not be counted as 'javascript'.
    If no matching posts are found or if the subreddit is invalid, the function prints nothing.

    Args:
        subreddit (str): The subreddit to query.
        word_list (list): A list of keywords to count in article titles.
        after (str): The identifier for the next page of results. Defaults to an empty string.
        word_dict (dict): A dictionary to store the count of keywords. Defaults to an empty dictionary.

    Returns:
        None
    """

    # Initialize the word count dictionary if it's empty
    if not word_dict:
        for word in word_list:
            if word.lower() not in word_dict:
                word_dict[word.lower()] = 0

    # Base case: if 'after' is None, print the sorted word counts
    if after is None:
        sorted_word_counts = sorted(word_dict.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_word_counts:
            if count:
                print('{}: {}'.format(word, count))
        return None

    # Define the Reddit API URL and parameters
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    headers = {'User-Agent': 'redquery'}
    params = {'limit': 100, 'after': after}

    # Make the API request
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    # If the response is not successful, return None
    if response.status_code != 200:
        return None

    # Process the API response
    try:
        data = response.json()['data']
        hot_articles = data['children']
        next_page = data['after']
        for article in hot_articles:
            title = article['data']['title']
            words_in_title = [word.lower() for word in title.split()]

            # Count the occurrences of each keyword in the title
            for word in word_dict.keys():
                word_dict[word] += words_in_title.count(word)

    except Exception:
        return None

    # Recursively call the function with the next page of results
    count_words(subreddit, word_list, next_page, word_dict)

