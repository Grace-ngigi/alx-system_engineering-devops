#!/usr/bin/python3
"""
queries the Reddit API
returns the a list containing titles of hot articles for a subreddit
"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    if after:
        url += "&after={}".format(after)

    headers = {"user-Agent": "MyRedditBot/1.0 someone_interesting"}
    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code == 200:
        data = res.json()
        posts = data.get('data', {}).get('children', [])

        if posts:
            for post in posts:
                title = post['data']['title']
                hot_list.append(title)
            # Recursive calls
            after = data['data']['after']
            if after:
                recurse(subreddit, hot_list, after)
        else:
            # base case: no more posts
            return hot_list
    else:
        return None
