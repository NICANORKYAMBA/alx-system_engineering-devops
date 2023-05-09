#!/usr/bin/python3
"""Queries the Reddit API, parses the title of all hot
articles, and prints a sorted count of given keywords
(case-insensitive, delimited by spaces
"""
import requests


def count_words(subreddit, word_list, after=None, counts={}):
    """
    Queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords
    (case-insensitive, delimited by spaces).
    """
    if not after:
        counts = {word.lower(): 0 for word in word_list}
        after = ""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyUserAgent 1.0"}
    params = {"after": after, "limit": 100}
    response = requests.get(
            url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        print("Invalid subreddit or no matching posts found.")
        return

    data = response.json()["data"]
    after = data.get("after")

    for post in data.get("children"):
        title = post.get("data").get("title").lower()
        for word in word_list:
            word_count = title.count(word.lower())
            counts[word.lower()] += word_count

    if after:
        count_words(subreddit, word_list, after, counts)
    else:
        counts = {word: count for word, count in counts.items() if count > 0}
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word}: {count}")
