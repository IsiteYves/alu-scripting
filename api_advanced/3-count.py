#!/usr/bin/python3
"""
Module containing a recursive function to parse titles of hot articles
and display a sorted count of given keywords.
"""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Queries Reddit API recursively, parses titles of all hot articles,
    and prints a sorted count of given keywords (case-insensitive).
    """
    if counts is None:
        # Initialize dictionary to keep track of lowercased target words
        counts = {}
        for word in word_list:
            w_lower = word.lower()
            counts[w_lower] = counts.get(w_lower, 0)

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "ALU-Student-Reddit-Script-v1.0"}
    params = {"limit": 100}
    if after:
        params["after"] = after

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code != 200:
            return

        data = response.json()
        children = data.get("data", {}).get("children", [])

        # Process each post title
        for post in children:
            title = post.get("data", {}).get("title", "")
            # Split by whitespace, convert words to lower case
            words_in_title = [w.lower() for w in title.split()]
            for word in words_in_title:
                # To prevent matches with punctuation, strip non-alphanumeric
                # but match the exact word rules from task requirements
                cleaned_word = word.strip("!@#$%^&*()-_+={}[]|\\:;'\",.<>/?`~")
                if cleaned_word in counts:
                    counts[cleaned_word] += 1

        next_after = data.get("data", {}).get("after")
        if next_after:
            return count_words(subreddit, word_list, next_after, counts)

        # Base case reached: no more pages, format and print results
        # Filter out words with 0 counts
        filtered_counts = {k: v for k, v in counts.items() if v > 0}
        if not filtered_counts:
            return

        # Sort: first by count descending, then alphabetically ascending
        sorted_results = sorted(
            filtered_counts.items(),
            key=lambda item: (-item[1], item[0])
        )

        for keyword, count in sorted_results:
            print("{}: {}".format(keyword, count))

    except Exception:
        return
