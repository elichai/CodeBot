import os
from os.path import join
dirname = os.path.dirname(__file__)

OWNER = 1041389880046219264

with open(join(dirname, 'twitter.pubkey'), 'r') as f:
    TWITTER_CONSUMER_KEY = f.read().replace('\n', '')

with open(join(dirname, 'twitter.privkey'), 'r') as f:
    TWITTER_CONSUMER_SECRET = f.read().replace('\n', '')

with open(join(dirname, 'access.token'), 'r') as f:
    TWITTER_ACCESS_TOKEN = f.read().replace('\n', '')

with open(join(dirname, 'access-secret.token'), 'r') as f:
    TWITTER_ACCESS_TOKEN_SECRET = f.read().replace('\n', '')
