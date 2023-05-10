#!/usr/bin/python3
"""Queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """Recursively queries the Reddit API and returns a
    list containing the titles of all hot articles
    for a given subreddit.

    Args:
        subreddit (str): The subreddit to search for.
        hot_list (list, optional): The list of hot article
        titles to be returned. Defaults to None.
        after (str, optional): The parameter that will
        indicate the starting point for the next page
        of results. Defaults to None.

    Returns:
        list: A list of hot article titles for the given
        subreddit.
    """
    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-agent': 'Mozilla/5.0'}

    """
    Set the 'after' parameter to start at the beginning of
    the results or to continue from the last page
    """
    params = {'limit': 100}
    if after:
        params['after'] = after

    """
    Make the API request and parse the JSON response
    """
    response = requests.get(
            url, headers=headers, params=params, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()['data']
        hot_list += [post['data']['title'] for post in data['children']]

        """
        Recursively call the function with the 'after' parameter
        set to the next page's starting point
        """
        if data['after']:
            recurse(subreddit, hot_list, after=data['after'])

        return hot_list
    elif response.status_code == 404:
        return None
    else:
        raise Exception("Request failed with status code {}.".format(
            response.status_code))
