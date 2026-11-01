#!/usr/bin/python3
"""Module that queries the Reddit API for a subreddit's hot posts."""

import requests


def top_ten(subreddit):
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "api.advanced:anything (by /u/shyakacarrick)"}
    params = {"limit": 10}

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False,
            timeout=10
        )
        if response.status_code != 200:
            print(None)
            return
        posts = response.json().get("data", {}).get("children", [])
    except (requests.exceptions.RequestException, ValueError):
        print(None)
        return

    for post in posts[:10]:
        print(post.get("data", {}).get("title"))
