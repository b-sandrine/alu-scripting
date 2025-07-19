#!/usr/bin/python3

""" 
0-subs Returns number of subscribers for a subreddit, or 0 if invalid
"""

import requests

def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given subreddit."""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {
            "User-Agent: RedditScript/0.1 by sandrine_d"
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
