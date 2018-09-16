import tweepy
from CodeBot.keys import OWNER
import hashlib
from CodeBot.executor import Executor

class MyStreamListener(tweepy.StreamListener):

    def special_handle(self, text):
        if text == 'whoami':
            return "@elichai2 @isan_rivkin"
        if text == 'help':
            return "@isan_rivkin Please Add Help"
        return None

    def on_status(self, status):
        # TODO: Do something with results
        if status.author.id == OWNER:  # Return if I'm the poster.
            return

        if hasattr(status, 'extended_tweet'):
            tweet = status.extended_tweet['full_text']
        else:
            tweet = status.text

        if tweet[:10] == '@CodeBot5 ':
            tweet = tweet[10:]
        else:
            tweet = tweet
        test_special = self.special_handle(tweet)
        if test_special is not None:
            self.reply(test_special, status.id_str)
            return

        executeer = Executor("continuumio/anaconda3")
        print(tweet)
        response = executeer.execute(tweet, timeout=False)
        print(response)
        print("hi")
        response = "@" + status.author.screen_name + ' ' + response
        self.reply(response, status.id_str)

    def reply(self, response, id):
        if len(response) <= 280:
            self.api.update_status(response, in_reply_to_status_id=id)
        else:
            pass


    def on_error(self, status_code):
        if status_code == 420:
            # TODO: Retry?
            # returning False in on_error disconnects the stream
            return False