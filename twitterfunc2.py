# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 15:48:04 2023

@author: dorie
"""



      
import base64
import hashlib
import os
import re
import requests
import tweepy

from requests_oauthlib import OAuth2Session
from flask import Flask, request, redirect, session, url_for, render_template


app = Flask(__name__)
app.secret_key = os.urandom(50)


CLIENT_ID='Q05kTVRPSjJGMVVvcjRUX2VqS2g6MTpjaQ'
CLIENT_SECRET='F3edjZfuH8nlOAg0sWpbLNMa95QKJ2525YA8FOTXh7IEUNZeVP'
REDIRECT_URI='http://127.0.0.1:5000/oauth/callback'

client_id = 'Q05kTVRPSjJGMVVvcjRUX2VqS2g6MTpjaQ'
client_secret = 'F3edjZfuH8nlOAg0sWpbLNMa95QKJ2525YA8FOTXh7IEUNZeVP'
auth_url = "https://twitter.com/i/oauth2/authorize"
token_url1 = "https://api.twitter.com/2/oauth2/token"
redirect_uri = os.environ.get("REDIRECT_URI")

scopes = ["tweet.read", "users.read", "tweet.write"]

code_verifier = base64.urlsafe_b64encode(os.urandom(30)).decode("utf-8")
code_verifier1 = re.sub("[^a-zA-Z0-9]+", "", code_verifier)

code_challenge = hashlib.sha256(code_verifier.encode("utf-8")).digest()
code_challenge = base64.urlsafe_b64encode(code_challenge).decode("utf-8")
code_challenge = code_challenge.replace("=", "")


API_KEY='UdQkXO0zpWMYzfHdHOzHshqbj'
API_SECRET='5n4Ad5lG97jOjdOieUrBNt0JfUfCaZV0pZ7LiIQN0iHmZSZcc0'
ACCESS_TOKEN='1710771170315022336-kV6Xm02mtKTYaJKpBxUo1zgwWySLti'
ACCESS_TOKEN_SECRET='rsVKuWrFOnT5KLCXeAaBCpN0iIF5h1j1k52y2QZPhaacG'
    
def upload_media():
    tweepy_auth = tweepy.OAuth1UserHandler(
        "{}".format(os.environ.get("API_KEY")),
        "{}".format(os.environ.get("API_SECRET")),
        "{}".format(os.environ.get("ACCESS_TOKEN")),
        "{}".format(os.environ.get("ACCESS_TOKEN_SECRET")),
    )
    tweepy_api = tweepy.API(tweepy_auth)
    url = "https://api.thecatapi.com/v1/images/search"
    cats = requests.request("GET", url).json()
    cat_pic = cats[0]["url"]
    img_data = requests.get(cat_pic).content
    with open("catpic.jpg", "wb") as handler:
        handler.write(img_data)
    post = tweepy_api.simple_upload("catpic.jpg")
    text = str(post)
    media_id = re.search("media_id=(.+?),", text).group(1)
    payload = {"media": {"media_ids": ["{}".format(media_id)]}}
    os.remove("catpic.jpg")
    return payload

      
def post_tweet(payload, new_token):
    print("Tweeting!")
    return requests.request(
        "POST",
        "https://api.twitter.com/2/tweets",
        json=payload,
        headers={
            "Authorization": "Bearer {}".format(new_token["access_token"]),
            "Content-Type": "application/json",
        },
    )

      

if __name__=='__main__':
    #code = request.args.get("code")
    code=CLIENT_SECRET
    twitter = OAuth2Session(CLIENT_ID, redirect_uri=redirect_uri, scope=scopes)
    authorization_url, state = twitter.authorization_url(
    auth_url, code_challenge=code_challenge, code_challenge_method="S256"
    )
    #session["oauth_state"] = state
    token = twitter.fetch_token(
    token_url=token_url1,
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    code_verifier=code_verifier1,
    code=code,
    )
    post_tweet('first tweet',token)
    

    



    

