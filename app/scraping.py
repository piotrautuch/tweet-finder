import tweepy
from app import app

def getTweet(keyword):
    # Setting variables by opening a textfile with relevant passages
    with open("tweetapi.txt") as f:
        access_file = f.read().splitlines()
    consumer_key = access_file[0]
    consumer_secret = access_file[1]

    access_token = access_file[2]
    access_token_secret = access_file[3]

    # Authenticate
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Setting a connection
    #api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
    api = tweepy.API(auth)
    # Looking for tweets
    public_tweets = api.search(keyword, tweet_mode='extended')
    # Returning the data
    try:
        return public_tweets
    except IndexError:
        return None
