import tweepy
from CodeBot.twitter_listener import MyStreamListener
from CodeBot.keys import *


def listen(api):
    my_streamer = MyStreamListener(api)
    my_stream = tweepy.Stream(auth=api.auth, listener=my_streamer, async=True)
    my_stream.filter(follow=[str(OWNER)])
    return my_stream


def start():
    auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    stream = listen(api)
    stream._thread.join()

