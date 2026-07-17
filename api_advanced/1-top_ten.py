#!/usr/bin/python3
"""
Module containing a function to print the titles of the first 10 hot posts.
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit. Prints None if the subreddit is invalid.
    """
    if not subreddit or not isinstance(subreddit, str):
        print("None")
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    # A highly unique User-Agent prevents Reddit from returning 429/302 blocks
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/111.0.0.0 Safari/537.36 "
                      "ALU-Scripting-Project-v2.0"
    }
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            children = data.get("data", {}).get("children", [])
            if not children:
                print("None")
                return
            for post in children:
                print(post.get("data", {}).get("title"))
        else:
            print("None")
    except Exception:
        print("None")
