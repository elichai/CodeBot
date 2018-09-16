import tweepy
from CodeBot.keys import OWNER
import hashlib

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        # TODO: Do something with results
        if status.author.id == OWNER:  # Return if I'm the poster.
            return

        if status.extended_tweet['full_text'][:10] == '@CodeBot5 ':
            response = status.extended_tweet['full_text'][10:]
        else:
            response = status.extended_tweet['full_text']

        print(response)
        m = hashlib.sha256()
        m.update(response.encode())
        response = m.hexdigest()
        response = "@" + status.author.screen_name + ' ' + response
        self.reply(response, status.id_str)

    def reply(self, response, id):
        print(self.api.update_status(response, in_reply_to_status_id=id))

    def on_error(self, status_code):
        if status_code == 420:
            # TODO: Retry?
            # returning False in on_error disconnects the stream
            return False