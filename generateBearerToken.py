# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 16:38:50 2023

@author: dorie
"""

import requests
import base64

# Credentials
API_KEY = 'UdQkXO0zpWMYzfHdHOzHshqbj'
API_SECRET = '5n4Ad5lG97jOjdOieUrBNt0JfUfCaZV0pZ7LiIQN0iHmZSZcc0'

# 1. Create Base64 encoded key
key_secret = f"{API_KEY}:{API_SECRET}".encode('ascii')
b64_encoded_key = base64.b64encode(key_secret)
b64_encoded_key = b64_encoded_key.decode('ascii')

# 2. Obtain Bearer Token
BASE_URL = 'https://api.twitter.com/'
AUTH_URL = f"{BASE_URL}oauth2/token"

headers = {
    'Authorization': f'Basic {b64_encoded_key}',
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
}

data = {
    'grant_type': 'client_credentials'
}

response = requests.post(AUTH_URL, headers=headers, data=data)
if response.status_code == 200:
    token_data = response.json()
    BEARER_TOKEN = token_data['access_token']
    print("Bearer Token:", BEARER_TOKEN)
else:
    print(f"Error {response.status_code}: Failed to obtain Bearer Token.")
    print(response.text)
    
    
URL = "https://api.twitter.com/2/tweets"

headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}",
    "Content-Type": "application/json"
}

def create_tweet(text):
    payload = {
        "status": text
    }
    response = requests.post(URL, headers=headers, json=payload)
    if response.status_code == 201:
        print(f"Successfully created tweet with ID: {response.json()['data']['id']}")
    else:
        print(f"Error {response.status_code}: {response.text}")

if __name__ == '__main__':
    tweet_text = input("Enter your tweet: ")
    create_tweet(tweet_text)