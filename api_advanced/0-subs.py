#!/usr/bin/python3
"""Reddit API subscriber counter"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': 'python:sub.count.script:v1.0 (by /u/your_reddit_username)'
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data.get('data', {}).get('subscribers', 0)
        else:
            # Print error for debugging (optional)
            # print(f"Error: Status code {response.status_code}")
            return 0
    except requests.RequestException:
        return 0
