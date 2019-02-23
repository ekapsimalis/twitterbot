import tweepy
from sys import exit

credentialstxt = 'data\\credentials.txt'
    
f_read = open(credentialstxt, 'r')
crds = f_read.read().strip()
credentials = []
credentials = crds.split(",")
f_read.close()


try:
    print("TRYING TO AUTHENDICATE YOU...")
    auth = tweepy.OAuthHandler(credentials[0], credentials[1])
    auth.set_access_token(credentials[2], credentials[3])
    api = tweepy.API(auth)
    user = api.me()
    print("AUTH SUCCESS!")
except tweepy.TweepError as e:
    print(e.reason)
    exit()
