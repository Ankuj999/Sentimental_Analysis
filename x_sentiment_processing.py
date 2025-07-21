import nltk
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

def classify_sentiment(text):
    scores = sia.polarity_scores(text)
    compound_score = scores['compound']
    
    if compound_score >= 0.05:
        return "Positive"
    elif compound_score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

# # Example usage
# print(classify_sentiment("I absolutely love this!"))  # Positive
# print(classify_sentiment("This is okay, nothing special."))  # Neutral
# print(classify_sentiment("I really hate this, it's terrible!"))  # Negative

# df1 = pd.read_csv("./AAP_tweets_cleaned.csv")
# df2 = pd.read_csv("./AAP_tweets_cleaned2.csv")
# # print(df.columns)
# df1["sentiment"] = df1["clean_text"].apply(classify_sentiment)
# print(df1.head())
# df2["sentiment"] = df2["clean_text"].apply(classify_sentiment)
# print(df2.head())
# df1.to_csv("./sentiment_output1.csv", index=False)
# print(df1.head())
# df2.to_csv("./sentiment_output2.csv", index=False)
# print(df2.head())

df = pd.read_csv("./AAP_tweets_cleaned_self.csv")
df["sentiment"] = df["clean_text"].apply(classify_sentiment)
print(df.head())
df.to_csv("./x_sentiment_output_self.csv", index=False)