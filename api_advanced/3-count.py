#!/usr/bin/python3
"""Module for count_words function"""
import requests


def count_words(subreddit, word_list, after=None, word_dic=None):
    if word_dic is None:
        word_dic = {}
        for word in word_list:
            word_dic[word.lower()] = 0

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "api.advanced:anything (by /u/shyakacarrick)"
    }
    params = {
        "after": after
    }
    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code != 200:
        return

    data = response.json().get("data", {})
    after = data.get("after")
    posts = data.get("children", [])

    for post in posts:
        title = post.get("data", {}).get("title", "")
        words = title.lower().split()
        for word in words:
            for search_word in word_list:
                if word == search_word.lower():
                    word_dic[word] += 1

    if after is not None:
        return count_words(subreddit, word_list, after, word_dic)
    else:
        sorted_words = sorted(
            word_dic.items(), key=lambda kv: (-kv[1], kv[0])
        )
        for k, v in sorted_words:
            if v > 0:
                print("{}: {}".format(k, v))
