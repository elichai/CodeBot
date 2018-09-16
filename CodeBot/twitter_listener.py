import tweepy


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        # TODO: Do something with results
        print(status.text)

    def on_error(self, status_code):
        if status_code == 420:
            # TODO: Retry?
            #returning False in on_error disconnects the stream
            return False