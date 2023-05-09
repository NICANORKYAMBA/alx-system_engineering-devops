#!/usr/bin/python3
"""
Returns the number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns number of subscribers for a given subreddit
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    """
    Set the URL for the Reddit API endpoint that provides
    information about the subreddit
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    """
    Set a custom User-Agent header to identify the script
    making the request
    """
    headers = {'User-Agent': 'MyCustomUserAgent/1.0'}

    """
    Send a GET request to the Reddit API endpoint with
    the custom headers
    """
    response = requests.get(url, headers=headers)

    data = response.json()

    try:
        return data['data']['subscribers']
    except Exception:
        return 0
