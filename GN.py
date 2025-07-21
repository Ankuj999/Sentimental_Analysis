from GoogleNews import GoogleNews
import pandas as pd

# Initialize GoogleNews scraper
googlenews = GoogleNews(lang='en', period='7d')  # Fetch news from last 7 days

# Search for AAP Election loss news
googlenews.search("AAP Delhi Election Loss")

# Get results
news_results = googlenews.result()
data1 = []

for news in news_results:
    data1.append([news['date'], news['title'], news['link']])

# Save to DataFrame
df = pd.DataFrame(data1, columns=['Date', 'Title', 'Link'])
print(df.head())

# Save as CSV
df.to_csv("AAP_news_data.csv", index=False)
print(df)

from GoogleNews import GoogleNews
import pandas as pd
googlenews = GoogleNews(lang='en', period='7d')

googlenews.search("Delhi Election")

news_results = googlenews.result()
data2 = []

df = pd.DataFrame(data2, columns=['Date', 'Title', 'Link'])
print(df.head())

# Save as CSV
df.to_csv("AAP_news_data.csv", index=False)
print(df)




from GoogleNews import GoogleNews
import pandas as pd

googlenews = GoogleNews(lang='en', period='30d')  # Fetch news from the last 30 days
googlenews.search("AAP Delhi Election Loss")

# Collect multiple pages of results
data = []
for i in range(50):  # Fetch first 5 pages of news
    googlenews.get_page(i)
    news_results = googlenews.result()
    for news in news_results:
        data.append([news.get('date', 'N/A'), news.get('title', 'N/A'), news.get('link', 'N/A')])

# Convert to DataFrame
df = pd.DataFrame(data, columns=['Date', 'Title', 'Link'])
df.drop_duplicates(inplace=True)  # Remove duplicate articles

# Save to CSV
df.to_csv("AAP_news_data2.csv", index=False)
print(df.head())