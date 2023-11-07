#!/usr/bin/python3
""" This script queries the Reddit API
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
        returns a list containing the titles of all hot articles for
        a given subreddit
        Args:
            subreddit (str): subreddit
            hot_list (list): hot_list
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'custom'}

    if after:
        url += "?after={}".format(after)

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return None

    data = response.json()['data']
    hot_list.extend(post['data']['title'] for post in data['children'])

    if data['after']:
        return recurse(subreddit, hot_list, data['after'])

    return hot_list
