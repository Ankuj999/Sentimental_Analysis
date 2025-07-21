import tweepy
import pandas as pd

# Replace with your Bearer Token
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAMOIzQEAAAAA1UG%2FS54yegxMFFBEYXRK8KBbatc%3DOnkigY4XU0d3i8KYL7Iy8UENrfR3N4unFOVMUcq5qOnzdq5Ayo"

# Initialize client
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# Define search query
query = "AAP Delhi Election -is:retweet lang:en"

# Fetch tweets (max 10 due to free API limitations)
tweets = client.search_recent_tweets(query=query, max_results=10, tweet_fields=["created_at", "text", "author_id"])

# Extract data
data = []
for tweet in tweets.data:
    data.append([tweet.created_at, tweet.text, tweet.author_id])

# Convert to DataFrame
df = pd.DataFrame(data, columns=["Date", "Tweet", "Author ID"])
df.to_csv("AAP_tweets.csv", index=False)

print(df.head())  # Check results
