import pandas as pd
df = pd.read_csv("./AAP_tweets5.csv")
# print(df.head())

import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords')
nltk.download('punkt_tab')
nltk.download('wordnet')

def clean_text(text):
    text = re.sub(r"http\S+|www\S+|https\S+", '', text, flags=re.MULTILINE)  # Remove URLs
    text = re.sub(r'\@\w+|\#', '', text)  # Remove @mentions and hashtags
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuations
    tokens = word_tokenize(text)  # Tokenization
    tokens = [WordNetLemmatizer().lemmatize(word) for word in tokens if word not in stopwords.words('english')]  # Lemmatization
    return " ".join(tokens)

df["clean_text"] = df["text"].apply(clean_text)
print(df.head())
df.to_csv("./AAP_tweets_cleaned_self.csv", index=False)