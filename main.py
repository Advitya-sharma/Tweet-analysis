from textblob import TextBlob
import sys,tweepy
import matplotlib.pyplot as plt
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud,STOPWORDS 
import seaborn as sns



consumerKey = "" #enter your consumerKey
consumerSecret = "" #enter your consumerSecret

accessToken = "" #enter your accessToken
accesssecret = "" #enter your accesssecret

auth = tweepy.OAuthHandler(consumer_key=consumerKey,consumer_secret=consumerSecret)
auth.set_access_token(accessToken,accesssecret) 
api = tweepy.API(auth)


tweet = tweepy.Cursor(api.search, q="lpuuniversity",tweet_mode="extended",lang = "en",count=200,include_rts=False).items(100)

df = pd.DataFrame([tweet.full_text for tweet in tweet],columns=['Tweets'])

print(df.head())

def cleantext(text):
    text = re.sub(r'@[A-Za-z)-9]+',"",text)
    text = re.sub(r'#','',text)
    text = re.sub(r'RT[\s]+',"",text)
    text = re.sub(r'https?:\/\/\S+',"",text)

    return text

df['Tweets'] = df['Tweets'].apply(cleantext)

stopwords = set(STOPWORDS) 

allwords = ' '.join([tweets for tweets in df['Tweets']])

plt.title("Wordcloud for 100 latest tweets")
wordcloud = WordCloud(width=500,height=300,max_font_size=112,stopwords = stopwords).generate(allwords)
plt.imshow(wordcloud)
plt.show()

def getPolarity(text):
    return TextBlob(text).sentiment.polarity

df['Polarity'] = df["Tweets"].apply(getPolarity)


def getAnalysis(score):

    if score < 0:
        return 'Negative'
    elif score == 0:
        return 'Neutral'
    else:
        return 'Positive'

df['Analysis'] = df["Polarity"].apply(getAnalysis)

plt.title("Sentiment Analysis")

print(df.head())

plt.style.use('ggplot')

df["Analysis"].value_counts().plot(kind='bar')
plt.xticks(rotation='horizontal')
plt.show()
