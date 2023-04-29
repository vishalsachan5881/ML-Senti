
import tweepy

# Set up your Twitter API credentials
consumer_key= "fsKm9fDDukcG3tALaNATWJ7u4"
consumer_secret="T1gPPxgRq6qKeim2lSpxgZDrsBBA2r4ejc6iFaGxqe1Xn7c6h5"
access_token= "1341683453541064704-F9oKrvxoLxO6STKIwS6rqF8i3SSd1C"
access_token_secret= "OyQnHjrT4VjlBnKOCDMnKkiuWSfdltSmmAygtAgpqVBE0"

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True)

# Define movie-related query parameters
movie_name = 'Pathaan'  # Replace with the name of the movie you want to search for
tweet_count = 100  # Number of tweets to retrieve per API call
max_tweets = 10000  # Maximum number of tweets to retrieve (adjust as needed)

# Retrieve tweets
tweets = tweepy.Cursor(api.search_tweets, q=movie_name, lang='en', tweet_mode='extended').items(max_tweets)

# Extract relevant information from tweets
tweet_texts = [tweet.full_text for tweet in tweets]  # Extract full text of tweets

# Print the retrieved tweets
for i, tweet_text in enumerate(tweet_texts):
    print(f'Tweet {i+1}: {tweet_text}')
