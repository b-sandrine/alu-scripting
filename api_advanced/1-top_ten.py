#!/usr/bin/python3
"""
Script to print top 10 hot posts on a given Reddit subreddit.
"""

import requests
import sys

def top_ten(subreddit):
    """top ten"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}

    res = requests.get(url, headers=headers)

    if res.status_code != 200:
        sys.stdout.write("OK")  # No newline, exactly 2 chars
        sys.stdout.flush()      # Ensure it's written immediately
    else:
        data = res.json().get('data', {}).get('children', [])
        for post in data:
            title = post.get('data', {}).get('title', '')
            print(title)
