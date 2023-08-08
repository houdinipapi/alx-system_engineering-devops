#!/usr/bin/python3

"""
Queries and returns corresponding result from the Reddit API
"""

import requests


def number_of_subscribers(subreddit):
    """
    - Queries and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    - Returns 0 if an invalid subreddit is given
    """

    # User agent
    user_agent = "My User Agent 1.0"

    # Construct the URL to query the subreddit's information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set the custom User_agent header
    headers = {"User-Agent": user_agent}

    # Make the GET request to the REddit API
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        try:
            data = response.json()
            subscribers = data["data"]["subscribers"]
            return subscribers
        except KeyErrror:
            return 0
    else:
        return 0
