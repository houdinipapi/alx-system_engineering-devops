#!/usr/bin/python3

"""
Top 10 hot posts
"""

from requests import get


def top_ten(subreddit):
    """
    - Queries the Reddit API
    - Prints the titles of the first 10 hot posts
    listed for a given subreddit.
    """

    # User agent
    user_agent = "Mozilla/5.0"

    # URL to query the subreddit's information
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Custom user_agent header
    headers = {"User-Agent": user_agent}

    # Limiting parameters
    params = {"limit": 10}

    # Response
    response = get(url, headers=headers, allow_redirects=False,
                   params=params)

    if response.status_code != 200:
        print(None)
        return

    top_10 = response.json()["data"]["children"]
    [print(post["data"]["title"]) for post in top_10]
