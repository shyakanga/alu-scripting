#!/usr/bin/python3
"""Module for top_ten function"""
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "api.advanced:anything (by /u/shyakacarrick)"
    }
    response = requests.get(
        url,
        headers=headers,
        allow_redirects=False
    )

    if response.status_code == 200:
        posts = response.json().get("data", {}).get("children", [])
        for post in posts[:10]:
            print(post.get("data", {}).get("title"))
    else:
        print(None)
