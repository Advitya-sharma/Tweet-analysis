from textblob import TextBlob
import sys,tweepy
import matplotlib.pyplot as plt


consumerKey = "XOxzythWu8hHzvnIapml2XH9O"
consumerSecret = "LR6DA85OwtFfCYeJpMxJV4SsO5ZIhjvYeZQedgHG4isrccSp6J"

accessToken = "1192097781667651585-XOcrN0aT1Mqjld3brLJhfdo6dHCeB6"
accesssecret = "GPgxpjF4YHJVxMjAHX92VfXDICjjK9SbRPlLMhSCk45b5"

auth = tweepy.OAuthHandler(consumer_key=consumerKey,consumer_secret=consumerSecret)
auth.set_access_token(accessToken,accesssecret) 
api = tweepy.API(auth)


for page in tweepy.Cursor(api.search, q="donaldtrump",lang = "en",count=200,include_rts=False).items(10):
    print(page.text)


