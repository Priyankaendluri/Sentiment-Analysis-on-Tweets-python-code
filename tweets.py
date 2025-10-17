import tweepy
from textblob import TextBlob
import pandas as pd

# -----------------------------
# Step 1: Twitter API Credentials
# -----------------------------
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Authenticate with Twitter
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# -----------------------------
# Step 2: Fetch Tweets
# -----------------------------
query = "Artificial Intelligence"  # topic
tweets = tweepy.Cursor(api.search_tweets, q=query, lang="en", tweet_mode='extended').items(50)

data = []
for tweet in tweets:
    text = tweet.full_text
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive"
    elif polarity == 0:
        sentiment = "Neutral"
    else:
        sentiment = "Negative"

    data.append([text, polarity, sentiment])

# -----------------------------
# Step 3: Create DataFrame
# -----------------------------
df = pd.DataFrame(data, columns=['Tweet', 'Polarity', 'Sentiment'])
print(df.head(10))

# -----------------------------
# Step 4: Summary
# -----------------------------
print("\nSentiment Counts:")
print(df['Sentiment'].value_counts())

# Save results
df.to_csv('tweet_sentiment_analysis.csv', index=False)
print("\nResults saved to tweet_sentiment_analysis.csv")
