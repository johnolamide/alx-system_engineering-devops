#!/usr/bin/python3
""" This script contains a function that queries the Reddit API
"""
import requests
import sys


def number_of_subscribers(subreddit):
    """
       Returns the number of Reddit Subscribers
       Args:
           subreddit (str): Reddit subreddit
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'custom'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    return response.json()['data']['subscribers']
