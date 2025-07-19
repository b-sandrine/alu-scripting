#!/usr/bin/python3

""" 
0-subs 
"""

import requests

def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given subreddit."""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {
            'User-Agent': 'MyRedditScript/1.0 (by u/Flaky_Party_2046)'
            }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        print(f"The response from reddit: {response}")
        if response.status_code == 200:
            data = response.json()
            return data.get('data', {}).get('subscribers', 0)
        else:
            return 0
    except requests.RequestException:
        return 0
