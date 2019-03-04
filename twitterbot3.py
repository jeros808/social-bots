
 
import tweepy, time, sys

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


 
phrase = "#failure is the end and is the beginning, the alpha and the omega #singularity"

for tweet in tweepy.Cursor(api.search, q='#failure').items():
    try:
        tweetId = tweet.user.id
        username = tweet.user.screen_name
        api.update_status("@" + username + " " + phrase, in_reply_to_status_id = tweetId)
        print ("Replied with " + phrase)
        time.sleep(15)

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break

            
            

        



