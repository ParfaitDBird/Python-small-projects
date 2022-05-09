import tweepy
import time
import re
import dbtest

cnx = dbtest.verconx()

auth = tweepy.OAuthHandler('insert your own token')
auth.set_access_token('insert your own token')
api = tweepy.API(auth)
public_tweets = api.home_timeline()
user = api.me()
usuario = api.get_user('GdlkTaste')
def limiter_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except:
        time.sleep(300)
numbersofTweets=400
def tweet_info():
    cont = 0
    artist_name = []
    image_url = []
    for tweet in tweepy.Cursor(api.user_timeline,id="GdlkTaste",tweet_mode="extended").items(numbersofTweets):
        try:
            id= tweet.id
            status = api.get_status(id)
            if 'media' in tweet.entities:
                artist_name.append(str(status.entities["user_mentions"][0]["screen_name"]))
                image_url.append(str(status.entities["media"][0]["media_url_https"]))
            else:
                artist_name.append(str(status.entities["user_mentions"][0]["screen_name"]))
                image_url.append(str('https://i.ytimg.com/vi/L67BwxevLkw/hqdefault.jpg'))
            cont=cont+1
            print(cont)
            if cont==150:
                time.sleep(300)
                cont=0
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
    print("Procediendo a enviar imagenes.")
    return (artist_name,image_url)