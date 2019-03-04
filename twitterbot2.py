
 
import tweepy, time, sys

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

 
for tweet in tweepy.Cursor(api.search, q='#failure').items():
    try:
       
        print('\nTweet by: @' + tweet.user.screen_name)

        # Retweet tweets as they are found
        tweet.favorite()
        tweet.retweet()

        print('Retweeted the tweet')

        time.sleep(1)
            

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break



