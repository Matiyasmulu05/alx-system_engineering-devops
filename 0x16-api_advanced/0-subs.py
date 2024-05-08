import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom User Agent'}

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        
        if 'error' in data:
            return 0
        
        subscribers = data['data']['subscribers']
        return subscribers
    except:
        return 0
