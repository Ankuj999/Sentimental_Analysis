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

df = pd.read_csv("./google_news_cleaned_self.csv")
df["sentiment"] = df["clean_text"].apply(classify_sentiment)
print(df.head())
df.to_csv("./google_news_sentiment_output_self.csv", index=False)