import tweepy

import pandas as pd

import threading

# Replace with your Bearer Token (from Twitter Developer Portal)
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAMOIzQEAAAAA1UG%2FS54yegxMFFBEYXRK8KBbatc%3DOnkigY4XU0d3i8KYL7Iy8UENrfR3N4unFOVMUcq5qOnzdq5Ayo"

def fetch_and_save_tweets():
    # Authenticate using OAuth2
    client = tweepy.Client(bearer_token=BEARER_TOKEN, wait_on_rate_limit=True)

    query = "AAP Delhi Election Loss -is:retweet lang:en"
    tweets_data = []
    # tweets = client.search_recent_tweets(query=query, max_results=100, tweet_fields=["created_at", "text", "author_id"])

    response = client.search_recent_tweets(
        query=query,
        max_results=100,  # Max allowed per request
        tweet_fields=["created_at", "text", "author_id"],
    )

    if response.data:
        tweets_data.extend(response.data)

    # Paginate using next_token
    while "next_token" in response.meta:
        next_token = response.meta["next_token"]
        
        # Fetch next page
        response = client.search_recent_tweets(
            query=query,
            max_results=100,
            next_token=next_token,  # Use the token to get the next page
            tweet_fields=["created_at", "text", "author_id"],
        )
        
        if response.data:
            tweets_data.extend(response.data)

    print(f"Total tweets collected: {len(tweets_data)}")

# print(tweets)

# for tweet in tweets.data:
#     # print(tweet.created_at, tweet.text)
#     print(tweet)
#     tweets_data.append({
#         "created_at": tweet.created_at,
#         "text": tweet.text,
#         "author_id": tweet.author_id,
#     })

# Sample tweet data (Assuming you stored it in a list of dictionaries)
# tweets_data = [
#     {"created_at": "2025-02-21", "text": "AAP’s defeat was unexpected!", "author_id": 12345},
#     {"created_at": "2025-02-20", "text": "Good to see change in Delhi politics!", "author_id": 67890},
# ]

# Convert to DataFrame
    df = pd.DataFrame(tweets_data)

    # Save as CSV
    df.to_csv("AAP_tweets5.csv", index=False)
    print("Tweets saved successfully")

if __name__ == "__main__":
    # Create and start thread
    tweet_thread = threading.Thread(target=fetch_and_save_tweets)
    tweet_thread.start()
    
    # Main thread continues other operations
    print("Main thread is free to perform other tasks...")
    
    # Wait for the tweet thread to complete if needed
    tweet_thread.join()
    print("Execution completed!")