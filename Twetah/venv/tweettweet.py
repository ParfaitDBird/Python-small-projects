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

search_string  = ['Game','Arknights']
numbersofTweets=2
'''
for tweet in tweepy.Cursor(api.search, search_string).items(1):
    try:
        print(tweet.text)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
'''


for tweet in tweepy.Cursor(api.user_timeline, api.search, search_string).items(20):
    try:
        if "Gacha" or "gacha" in tweet.text:
            #print(tweet.text)
            api.update_status("Por favoro ",tweet.id,"@Lietail")
            break
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break