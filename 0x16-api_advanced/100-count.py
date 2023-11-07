#!/usr/bin/python3
"""
"""
import requests
import re
from collections import Counter


def count_words(subreddit, word_list, after=None, word_counter=None):
    if word_counter is None:
        word_counter = Counter()

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    if after:
        url += f"?after={after}"
    headers = {'User-agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return

    data = response.json()
    titles = [entry['data']['title'] for entry in data['data']['children']]
    for title in titles:
        words = re.findall(r'\b\w+\b', title.lower())
        for word in words:
            if word in word_list:
                word_counter[word] += 1

    after = data['data'].get('after')
    if after:
        count_words(subreddit, word_list, after, word_counter)
    else:
        sorted_words = sorted(
            [(k, v) for k, v in word_counter.items() if v > 0],
            key=lambda x: (-x[1], x[0])
        )
        for word, count in sorted_words:
            print(f"{word}: {count}")
