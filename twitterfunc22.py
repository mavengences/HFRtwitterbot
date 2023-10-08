# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 16:37:18 2023

@author: dorie
"""

import requests
from requests_oauthlib import OAuth1

# Twitter API credentials
API_KEY = 'UdQkXO0zpWMYzfHdHOzHshqbj'
API_SECRET = '5n4Ad5lG97jOjdOieUrBNt0JfUfCaZV0pZ7LiIQN0iHmZSZcc0'
ACCESS_TOKEN = '1710771170315022336-kV6Xm02mtKTYaJKpBxUo1zgwWySLti'
ACCESS_TOKEN_SECRET = 'rsVKuWrFOnT5KLCXeAaBCpN0iIF5h1j1k52y2QZPhaacG'

# Endpoint URL for creating a tweet (based on Twitter V1.1 API)
URL = "https://api.twitter.com/1.1/statuses/update.json"

# Set up OAuth1 authentication
auth = OAuth1(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

def create_tweet(text):
    payload = {
        "status": text
    }
    response = requests.post(URL, auth=auth, data=payload)
    if response.status_code == 200:
        print(f"Successfully created tweet with ID: {response.json()['id']}")
    else:
        print(f"Error {response.status_code}: {response.text}")

if __name__ == '__main__':
    tweet_text = input("Enter your tweet: ")
    create_tweet(tweet_text)