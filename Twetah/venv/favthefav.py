import tweepy
import time
auth = tweepy.OAuthHandler('')
auth.set_access_token('')

api = tweepy.API(auth)

public_tweets = api.home_timeline()
user = api.me()

def limiter_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except:
        time.sleep(300)

search_string  = 'Gacha'
numbersofTweets=2
'''
for tweet in tweepy.Cursor(api.search, search_string).items(numbersofTweets):
status = api.get_status(id, tweet_mode="extended")
try:
    print(status.retweeted_status.full_text)
except AttributeError:  # Not a Retweet
    print(status.full_text)
'''
for tweet in tweepy.Cursor(api.followers,api.search, search_string).items(numbersofTweets):
    try:
        tweet.
        print('I liked the tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break