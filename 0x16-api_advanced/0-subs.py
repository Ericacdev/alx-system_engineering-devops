#!/usr/bin/python3
"""
Script that  queries the Reddit API
"""
import requests


def num_of_subscribers(subreddit):
    """
    returns the number of subscribers (not active users, total subscribers)
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    results = response.json().get('data')
    return results.get('subscribers')
