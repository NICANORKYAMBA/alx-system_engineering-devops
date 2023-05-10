#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit
    """
    if subreddit is None or not isinstance(subreddit, str):
        print("None")
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 10}

    response = requests.get(
            url, headers=headers, params=params, allow_redirects=False)
    data = response.json()

    try:
        for post in data['data']['children']:
            print(post['data']['title'])
    except Exception:
        print("None")
