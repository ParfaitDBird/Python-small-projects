#Datos predeterminados.
import tweepy
import time
import re
import arttable
from arttable_imp import prueba
def fetchdb():
    auth = tweepy.OAuthHandler('')
    auth.set_access_token('')
    api = tweepy.API(auth)
    public_tweets = api.home_timeline()
    user = api.me()
    usuario = api.get_user('GdlkTaste')
    # Fin de Datos predeterminados.


    def limiter_handler(cursor):
        try:
            while True:
                yield cursor.next()
        except:
            time.sleep(300)

    numbersofTweets=500
    def tweet_info():
        cont = 0
        for tweet in tweepy.Cursor(api.user_timeline,id="GdlkTaste",tweet_mode="extended").items(numbersofTweets):
            try:
                id= tweet.id
                status = api.get_status(id)
                if 'media' and 'user_mentions' in tweet.entities:
                    aname=str(status.entities["user_mentions"][0]["screen_name"])
                    iurl=str(status.entities["media"][0]["media_url_https"])
                    prueba.insert(aname,iurl)
                else:
                    print("No se pudo insertar")
                cont=cont+1
                print(cont)
                if cont == 125:
                        print("espere 300 segundos.")
                        time.sleep(300)
                        cont = 0
                        print("Retomando proceso.")
            except tweepy.TweepError as e:
                print(e.reason)
            except KeyError:
                pass
            except IndexError:
                pass
            except StopIteration:
                break
        print("Procediendo a enviar imagenes.")
        return ("Tabla actualizada")

    log=tweet_info()
    print(log)