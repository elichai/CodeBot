with open('twitter.pubkey', 'r') as f:
    TWITTER_CONSUMER_KEY = f.read().replace('\n', '')

with open('twitter.privkey', 'r') as f:
    TWITTER_CONSUMER_SECRET = f.read().replace('\n', '')

with open('access.token', 'r') as f:
    TWITTER_ACCESS_TOKEN = f.read().replace('\n', '')

with open('access-secret.token', 'r') as f:
    TWITTER_ACCESS_TOKEN_SECRET = f.read().replace('\n', '')
