#!/usr/bin/python3
"""
queries the Reddit API
parses the title of all hot articles
prints a sorted count of given keywords
"""
import requests


def count_words(subreddit, word_list=None, after=None, word_counts=None):
    if word_counts is None:
        word_counts = {}

    if after is None:
        after = ""

    url = (
            "https://www.reddit.com/r/{}/hot.json?limit=100&after={}"
            .format(subreddit, after)
            )
    headers = {"user-Agent": "MyRedditBot/1.0 someone_interesting"}
    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code == 200:
        data = res.json()
        posts = data.get('data', {}).get('children', [])

        if posts:
            for post in posts:
                title = post['data']['title'].lower()
                for word in word_list:
                    if f" {word.lower()} " in f" {title} ":
                        word_counts[word.lower()] = (
                                word_counts.get(word.lower(), 0) + 1
                                )
            # Recursive calls
            after = data['data']['after']
            if after:
                count_words(subreddit, word_list, after, word_counts)
            else:
                # Base case: print results when there are no more posts
                sorted_word_counts = sorted(word_counts.items(),
                                            key=lambda x: (-x[1], x[0]))
                for word, count in sorted_word_counts:
                    print(f"{word}: {count}")
        else:
            # Base case: no more posts, print results
            sorted_word_counts = sorted(word_counts.items(),
                                        key=lambda x: (-x[1], x[0]))
            for word, count in sorted_word_counts:
                print(f"{word}: {count}")
    else:
        # Invalid subreddit or other error, print nothing
        pass
