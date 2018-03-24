
# coding: utf-8

# In[ ]:


# Dependencies
import tweepy
import json
import time

# Twitter API Keys
consumer_key = "JeOpBYvN38K6jwVKoQTuKhofj"
consumer_secret = "qNKYIpKRxVR95w3BzfD9CITJ2xhq7MM3I36yEqh2U6WsJAfB9q"
access_token = "975022209948413954-FxRMca7HQaLq01HP9YoXj3tk6HrHx2w"
access_token_secret = "gt4ZvTpOfSb69flVrWfLcEtpVmZCxhL0ly4BUq8n8GfUf"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Create a function that tweets
def TweetOut(tweet_number):

    api.update_status("Hi! This is tweet #%s!" % tweet_number)


# Create a loop that calls the TweetOut function every minute
counter = 0

# Infinite loop
while(True):

    # Call the TweetQuotes function and specify the tweet number
    TweetOut(counter)

    # Once tweeted, wait 60 seconds before doing anything else
    time.sleep(60)

    # Add 1 to the counter prior to re-running the loop
    counter = counter + 1

