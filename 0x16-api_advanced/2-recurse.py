#!/usr/bin/python3
"""
   Recursive fuction returns a list containing the titles of all hot articles for a given subreddit.
"""
import requests
from sys import argv


def recurse(subreddit, hot_list=[], after=""):
    """Return the titles of all host posts"""
    if after is None:
        return []

    url_sred_inf = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    url_sred_inf += "?limit=100&after={}".format(after)
    headers = {'user-agent': 'request'}
    response = requests.get(url_sred_inf, headers=headers,
                            allow_redirects=False)
    if str(response) != "<Response [200]>":
        return None
    r_json = response.json()
    hot_posts_json = r_json.get("data").get("children")
    for post in hot_posts_json:
        hot_list.append(post.get("data").get("title"))
    return hot_list + recurse(subreddit, [], r_json.get("data").get("after"))
