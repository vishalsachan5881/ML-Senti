import json
from twitter import Twitter, OAuth1BearerToken

# Configuration File
data = open("config.json")
config = json.load(data)

# Configuration Setup
bearer_token = OAuth1BearerToken("AAAAAAAAAAAAAAAAAAAAAAoSmwEAAAAAy9xmmWAJWZpZynF5FyAoOgavH5o%3DODYIAT6OOAxd0UWqWvzkKheNoivw7gifDk9eH4dUgWMTQEF3Wy")

# Configure the OAuth using the Credentials provided
twitter = Twitter(auth=bearer_token)

# Fetch the Tweets and query accordingly, filtered using links
try:
    tweets = twitter.search_all(
        query='#Pathaan -is:retweet',
        tweet_fields='public_metrics',
        expansions='author_id',
        max_results=100,
        start_time='2016-04-12T00:00:00Z',
        end_time='2016-04-13T00:00:00Z'
    )
except Exception as e:
    print("ERROR", e)

# List of the users who have already tweeted, so as to fetch tweets from different user every time
users_tweeted = []

# Tweet Count
i = 1

# For every tweet that is fetched, get only relevant tweets
for tweet in tweets['includes']['tweets']:
    user_id = tweet['author_id']
    if (user_id not in users_tweeted and tweet['public_metrics']['followers_count'] > 10):
        print(i, tweet['text'].encode(encoding='utf-8'))
        users_tweeted.append(user_id)
        i += 1
