from textblob import TextBlob
import sys,tweepy
import matplotlib.pyplot as plt
import pandas as pd
import re
from wordcloud import WordCloud

consumerKey = "XOxzythWu8hHzvnIapml2XH9O"
consumerSecret = "LR6DA85OwtFfCYeJpMxJV4SsO5ZIhjvYeZQedgHG4isrccSp6J"

accessToken = "1192097781667651585-XOcrN0aT1Mqjld3brLJhfdo6dHCeB6"
accesssecret = "GPgxpjF4YHJVxMjAHX92VfXDICjjK9SbRPlLMhSCk45b5"

auth = tweepy.OAuthHandler(consumer_key=consumerKey,consumer_secret=consumerSecret)
auth.set_access_token(accessToken,accesssecret) 
api = tweepy.API(auth)


tweet = tweepy.Cursor(api.search, q="JNU",tweet_mode="extended",lang = "en",count=200,include_rts=False).items(1000)

df = pd.DataFrame([tweet.full_text for tweet in tweet],columns=['Tweets'])

print(df.head())

def cleantext(text):
    text = re.sub(r'@[A-Za-z)-9]+',"",text)
    text = re.sub(r'#','',text)
    text = re.sub(r'RT[\s]+',"",text)
    text = re.sub(r'https?:\/\/\S+',"",text)

    return text

df['Tweets'] = df['Tweets'].apply(cleantext)

allwords = ' '.join([tweets for tweets in df['Tweets']])

wordcloud = WordCloud(width=500,height=300,max_font_size=112).generate(allwords)
plt.imshow(wordcloud)
plt.show()