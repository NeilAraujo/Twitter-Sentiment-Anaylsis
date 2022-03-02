from __future__ import print_function
import tweepy
import json
from pymongo import MongoClient

MONGO_HOST= 'mongodb://localhost:27017'  # assuming you have mongoDB installed locally
                                             # and a database called 'twitterdb'

WORDS = ['covid','corona','coronavirus','covid19']
LANGUAGES=['en']
# India
#LOCATION = [ 68.200623,  6.082298, 97.172252 ,33.821754]
# uk
#LOCATION=[-11.311065,48.922499,1.956421,58.478381]
# us
#LOCATION=[-124.712154,32.299516,-67.617097,42.185122]
# canada
#LOCATION=[-129.405755,43.665248,-57.166157,68.312743]
# australia
LOCATION=[111.475756,-40.758359,158.532706,-13.467990]

ACCESS_TOKEN = '948431034927984640-JW2BEoqSede6EEn4jJwovD6wmJmcuzI'
CONSUMER_KEY = 'XJG9lx0uzA8hzwpAMLhWfDGQP'
CONSUMER_SECRET = 'lKtDb6GkQZBCXZBYjT9iiQ3LF3Uybn4TnXLs0YHKfQl5Cuq7OQ'
ACCESS_TOKEN_SECRET = "vHc85lU3g3nIkiyl6EFW3oqjAzG1ZFfmNoOkoUX7qGjmE"


class StreamListener(tweepy.StreamListener):    
    #This is a class provided by tweepy to access the Twitter Streaming API. 

    def on_connect(self):
        # Called initially to connect to the Streaming API
        print("You are now connected to the streaming API.")
 
    def on_error(self, status_code):
        # On error - if an error occurs, display the error / status code
        print('An Error has occured: ' + repr(status_code))
        return False
 
    def on_data(self, data):
        #This is the meat of the script...it connects to your mongoDB and stores the tweet
        try:
            client = MongoClient(MONGO_HOST)
            
            # Use twitterdb database. If it doesn't exist, it will be created.
            db = client.twitterdb
    
            # Decode the JSON from Twitter
            datajson = json.loads(data)
            
            #grab the 'created_at' data from the Tweet to use for display
            created_at = datajson['created_at']

            #print out a message to the screen that we have collected a tweet
            print("Tweet collected at " + str(created_at))
            
            #insert the data into the mongoDB into a collection called twitter_search
            #if twitter_search doesn't exist, it will be created.
            db.australia.insert_one(datajson)
        except Exception as e:
           print(e)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
#Set up the listener. The 'wait_on_rate_limit=True' is needed to help with Twitter API rate limiting.
listener = StreamListener(api=tweepy.API(wait_on_rate_limit=True)) 
streamer = tweepy.Stream(auth=auth, listener=listener)
print("Tracking: " + str(WORDS))
streamer.filter(locations=LOCATION,languages=LANGUAGES,track=WORDS)
