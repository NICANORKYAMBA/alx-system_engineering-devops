#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""

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

    """
    If the response is successful, extract the number of
    subscribers from the JSON response
    """
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    """
    If the subreddit is invalid or the request fails, return 0
    """
    else:
        return 0
