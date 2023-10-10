#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
"""
import requests
import sys


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = { "user-Agent": "MyRedditBot/1.0 someone" }
    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code == 200:
        try:
            data = res.json()
            info = data['data']['subscribers']
            return info
        except (KeyError, ValueError):
            return 0
    elif res.status_code == 302:
        return 0
    else:
        return 0
