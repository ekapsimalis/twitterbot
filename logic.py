from auth import tweepy, api, user
import json

FILENAME = 'data\\numFollowers.txt'
LAST_SEEN_ID = 'data\\lastseenID.txt'

def totalFollowers():
    return user.followers_count

def follow_all():
    for follower in tweepy.Cursor(api.followers).items():
        follower.follow()
    print("Follow all my followers")

def searchbyNumbers(search):
    results = api.search(search, lang='el', show_user=True, tweet_mode='extended')
    for result in results:
        print(result.author.name + " ---> " + result.full_text + "|| " + str(result.created_at))


def retrieve(filename):
    f_read = open(filename, 'r')
    number = int(f_read.read().strip())
    f_read.close()
    return number

def retrieveLastSeenID(filename):
    f_read = open(filename, 'r')
    number = int(f_read.read().strip())
    f_read.close()
    return number

def store(num, filename):
    f_write = open(filename, 'w')
    f_write.write(str(num))
    f_write.close()
    return

def storeLastSeenId(num, filename):
    f_write = open(filename, 'w')
    f_write.write(str(num))
    f_write.close()
    return

def showChanges():
    last_seen_followers = retrieve(FILENAME)
    updated_followers = totalFollowers()
    if updated_followers == last_seen_followers:
        print("Followers number same as before: No new changes")
        return
    elif updated_followers > last_seen_followers:
        difference = updated_followers - last_seen_followers
        print("You gained " + str(difference) + " followers")
        store(str(updated_followers), FILENAME)
        return
    else:
        difference = last_seen_followers - updated_followers
        print("You lost " + str(difference) + " followers")
        store(updated_followers, FILENAME)
        return

def retreive_newest_mentions():
    last_id = retrieveLastSeenID(LAST_SEEN_ID)
    mentions = api.mentions_timeline(last_id, tweet_mode='extended')
    return mentions

def show_newest_mentions():       
    mentions = retreive_newest_mentions()
    if len(mentions) == 0:
        print("No new mentions")
    else:
        for mention in mentions:
            print("Displaying new mentions...")
            print("From: " + mention.author.name + " --> " + mention.full_text)
            storeLastSeenId(mention.id, LAST_SEEN_ID)

def show_trends():
    trends = api.trends_place(23424833)
    for trend in trends:
        for item in trend['trends']:
            if "#" in item['name']:
                print(item['name'])

def update_status(status):
    try:
        tweet = api.update_status(status)
        print("Tweet posted with text ---->" + tweet.text)
    except tweepy.error.TweepError as err:
        err.reason()

def delete_tweet(identifier):
    try:
        api.destroy_status(identifier)
        print("Tweet deleted")
    except tweepy.error.TweepError as err:
        err.reason()
    
