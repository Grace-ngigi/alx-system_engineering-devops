#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
"""
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    headers = {"user-Agent": "MyRedditBot/1.0 someone_interesting"}
    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code == 200:
        data = res.json()
        posts = data.get('data', {}).get('children', [])

        if posts:
            for post in posts:
                title = post['data']['title']
                print(title)
        else:
             print("None")
    else:
        print("None")
