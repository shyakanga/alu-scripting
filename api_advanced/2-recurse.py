#!/usr/bin/python3
"""Module for recurse function"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "api.advanced:anything (by /u/shyakacarrick)"
    }
    params = {
        "after": after
    }
    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )

    if response.status_code == 200:
        data = response.json().get("data", {})
        after = data.get("after")
        posts = data.get("children", [])
        for post in posts:
            hot_list.append(post.get("data", {}).get("title"))
        if after is not None:
            return recurse(subreddit, hot_list, after)
        return hot_list
    return None
