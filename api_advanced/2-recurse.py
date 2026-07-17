#!/usr/bin/python3
"""
Module containing a recursive function to fetch titles of all hot articles.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit. Returns None if invalid.
    """
    if not subreddit or not isinstance(subreddit, str):
        return None

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "ALU-Student-Reddit-Script-v1.0"}
    params = {"limit": 100}
    if after:
        params["after"] = after

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            children = data.get("data", {}).get("children", [])
            for post in children:
                hot_list.append(post.get("data", {}).get("title"))

            next_after = data.get("data", {}).get("after")
            if next_after:
                return recurse(subreddit, hot_list, next_after)
            return hot_list
        else:
            return None
    except Exception:
        return None
