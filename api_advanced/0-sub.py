#!/usr/bin/python3
"""Module for number_of_subscribers function"""
import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "api.advanced:anything (by /u/shyakacarrick)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return response.json().get("data", {}).get("subscribers", 0)

    return 0
