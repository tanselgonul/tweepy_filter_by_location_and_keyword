import sys
import tweepy

import twitterCredentials

auth = tweepy.OAuthHandler(twitterCredentials.CONSUMER_KEY, twitterCredentials.CONSUMER_SECRET)
auth.set_access_token(twitterCredentials.ACCESS_TOKEN,twitterCredentials.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        #if "--- some keyword to filter ---" in status.text.lower():
            print(status.text)
            with open('output.csv', 'a') as the_file:
                the_file.write(status.text + '\n')

    def on_error(self, status_code):
        print(sys.stderr)
        return True

    def on_timeout(self):
        print(sys.stderr)
        return True


sapi = tweepy.streaming.Stream(auth, CustomStreamListener())
sapi.filter(locations=[26.04, 35.82, 44.79, 42.14]) #turkey