import requests

def top_ten(subreddit):
    # Define the URL for the Reddit API
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    
    # Set headers to mimic a browser request and avoid rate limiting
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        # Make the API request without following redirects
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the response is a redirect (indicating invalid subreddit)
        if response.status_code == 301 or response.status_code == 302:
            print("None")
            return
        
        # Check if the response is successful
        if response.status_code != 200:
            print("None")
            return
            
        # Parse JSON response
        data = response.json()
        
        # Check if the subreddit exists and has posts
        if 'data' not in data or 'children' not in data['data']:
            print("None")
            return
            
        # Extract and print the titles of the first 10 posts
        posts = data['data']['children']
        if not posts:
            print("None")
            return
            
        for post in posts[:10]:
            title = post['data']['title']
            print(title)
            
    except requests.RequestException:
        print("None")
