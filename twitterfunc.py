# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 15:37:30 2023

@author: dorie
"""

import tweepy

# Replace with your Twitter API keys
consumer_key = "UdQkXO0zpWMYzfHdHOzHshqbj"
consumer_secret = "5n4Ad5lG97jOjdOieUrBNt0JfUfCaZV0pZ7LiIQN0iHmZSZcc0"
access_token = "1710771170315022336-kV6Xm02mtKTYaJKpBxUo1zgwWySLti"
access_token_secret = "rsVKuWrFOnT5KLCXeAaBCpN0iIF5h1j1k52y2QZPhaacG"

# Authenticate with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create an API object
api = tweepy.API(auth)



# Your tweet content
tweet_text = "Hello, Twitter! This is a test tweet using Tweepy and Python. #Python #Tweepy"

# Post the tweet
try:
    api.update_status(tweet_text)
    print("Tweet posted successfully!")
except Exception as e:
    print(f"Error: {e}")