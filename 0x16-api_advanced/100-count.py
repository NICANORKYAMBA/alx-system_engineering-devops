#!/usr/bin/python3
"""Queries the Reddit API, parses the title of all hot
articles, and prints a sorted count of given keywords
(case-insensitive, delimited by spaces
"""
import requests


def count_words(subreddit, word_list, after='', counts={}):
    """
    Queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords.

    Args:
    - subreddit (str): the subreddit to search for
    - word_list (list): a list of keywords to count
    - after (str): the identifier of the post to start the search after
    - counts (dict): a dictionary of counts for each keyword

    Returns:
    - None

    Note:
    - If word_list contains the same word (case-insensitive),
    the final count should be the sum of each duplicate.
    - Results should be printed in descending order,
    by the count, and if the count is the same for separate keywords,
    they should then be sorted alphabetically (ascending, from A to Z).
    - Words with no matches should be skipped and not printed.
    Words must be printed in lowercase.
    - Results are based on the number of times a keyword appears,
    not titles it appears in.
    """
    # Base case: if subreddit is invalid or there are no more posts
    if subreddit is None or not after:
        # Sort and print the word counts
        for word, count in sorted(counts.items(), key=lambda x: (-x[1], x[0])):
            print("{}: {}".format(word, count))
        return

    # Define the Reddit API endpoint
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    # Define the custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'Mozilla/5.0'}

    # Define the parameters for the Reddit API request
    params = {'after': after}

    # Send the request to the Reddit API
    response = requests.get(url, headers=headers, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON
        data = response.json()

        # Get the next post identifier for recursive calls
        next_after = data['data']['after']

        # Get the list of hot posts
        posts = data['data']['children']

        # Process each hot post
        for post in posts:
            # Get the title of the post
            title = post['data']['title']

            # Split the title into words
            words = title.lower().split()

            # Count the occurrences of each keyword in the title
            for word in word_list:
                # Check if the keyword is in the title
                if word.lower() in words:
                    # Add the keyword to the count dictionary
                    counts[word.lower()] = counts.get(word.lower(), 0) + 1

        # Recursive call with the next post identifier
        count_words(subreddit, word_list, next_after, counts)

    else:
        # Subreddit is invalid, print nothing
        print(None)
