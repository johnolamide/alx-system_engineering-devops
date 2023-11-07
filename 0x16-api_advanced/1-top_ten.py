#!/usr/bin/python3
""" This script queries the Reddit API
"""
import requests


def top_ten(subreddit):
    """
        Prints the title of he first 10 hot posts
        Args:
            subreddit (str): subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'custom'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    posts = response.json()['data']['children']
    for post in posts:
        print(post['data']['title'])
