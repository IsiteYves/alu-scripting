#!/usr/bin/python3
"""
Module containing a function to query Reddit API for subreddit subscribers.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit. If invalid, returns 0.
    """
    if not subreddit or not isinstance(subreddit, str):
        return 0

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "ALU-Student-Reddit-Script-v1.0"}

    try:
        # allow_redirects=False prevents automatic redirect to search page
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data.get("data", {}).get("subscribers", 0)
    except Exception:
        pass
    return 0
