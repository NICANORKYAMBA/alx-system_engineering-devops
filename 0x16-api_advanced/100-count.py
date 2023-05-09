#!/usr/bin/python3
"""Queries the Reddit API, parses the title of all hot
articles, and prints a sorted count of given keywords
(case-insensitive, delimited by spaces
"""
import requests


def count_words(subreddit, word_list, instances=None, after=None, count=0):
    """Prints counts of given words found in hot posts of a given subreddit.

    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        instances (dict): Key/value pairs of words/counts.
        after (str): The parameter for the next page of the API results.
        count (int): The parameter of results matched thus far.
    """
    if instances is None:
        instances = {}
    if after is None:
        url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    else:
        url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit) + "?count=" + str(count) + "&after=" + after
    headers = {
        "User-Agent": "myUserAgent"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return
    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        title = c.get("data").get("title").lower()
        for word in word_list:
            if (not word) or (word.lower() in title and
                    not any([c.lower() in title for c in "0123456789!@#$%^&*()_+={}[]|\:;\"<>,.?/~"])):
                times = title.count(word.lower())
                if word.lower() in instances:
                    instances[word.lower()] += times
                else:
                    instances[word.lower()] = times
    if after is not None:
        count_words(subreddit, word_list, instances, after, count)
    else:
        items = sorted(instances.items(), key=lambda x: (-x[1], x[0]))
        for item in items:
            print(item[0] + ": " + str(item[1]))
