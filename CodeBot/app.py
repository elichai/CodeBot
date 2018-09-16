import tweepy
from CodeBot.twitter_listener import MyStreamListener

with open('keys/twitter.pubkey', 'r') as myfile:
    TWITTER_CONSUMER_KEY = myfile.read().replace('\n', '')

with open('keys/twitter.privkey', 'r') as myfile:
    TWITTER_CONSUMER_SECRET = myfile.read().replace('\n', '')

with open('keys/access.token', 'r') as myfile:
    TWITTER_ACCESS_TOKEN = myfile.read().replace('\n', '')

with open('keys/access-secret.token', 'r') as myfile:
    TWITTER_ACCESS_TOKEN_SECRET = myfile.read().replace('\n', '')


auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

myStream.filter(follow=["1041389880046219264"])