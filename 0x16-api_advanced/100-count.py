#!/usr/bin/python3
"""Queries the Reddit API, parses the title of all hot
articles, and prints a sorted count of given keywords
(case-insensitive, delimited by spaces
"""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Prints counts of given words found in hot posts of a given subreddit
    """
    # Initialize counts dictionary on the first call of the function
    if counts is None:
        counts = {}
        for word in word_list:
            counts[word.lower()] = 0

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-agent': 'Mozilla/5.0'}
    params = {'limit': 100}
    if after:
        params['after'] = after

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        # Loop through each post and count occurrences of each keyword
        for post in posts:
            title = post['data']['title']
            words = title.lower().split()
            for word in word_list:
                if word.lower() in words:
                    counts[word.lower()] += words.count(word.lower())

        # Recursive call with after parameter to get next page of results
        after = data['data']['after']
        if after:
            count_words(subreddit, word_list, after=after, counts=counts)
        else:
            # Sort by count in descending order and then alphabetically
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                if count > 0:
                    print(f"{word}: {count}")
    else:
        print(f"Error getting data from {url}")
