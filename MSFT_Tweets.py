from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import twitter_credentials as tc

# Twitter Authenticator
class TwitterAuthenticator():
    def authenticate_twitter_app(self):
        auth = OAuthHandler(tc.consumer_key, tc.consumer_secret)
        auth.set_access_token(tc.access_token, tc.access_token_secret)
        return auth

class TwitterStreamer:
    # Class for streaming and processing live tweets

    # Constructor
    def __init__(self):
        self.twitter_authenticator = TwitterAuthenticator()


    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):

        # This handles the Twitter authentication and the connection to the Twitter Streaming API

        listener = TwitterListener(fetched_tweets_filename)
        auth = self.twitter_authenticator.authenticate_twitter_app()

        stream = Stream(auth, listener)

        # This line filters the tweets we want
        stream.filter(track=hash_tag_list)


class TwitterListener(StreamListener):

    # This is the basis listener class that prints received tweets to stdout

    def __init__(self, fetched_tweets_filename):
        self.fetch_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        try:
            print(data)
            with open(self.fetch_tweets_filename, 'a') as tf:
                tf.write(data)
                return True

        except BaseException as e:
            print("Error on data: %s" % str(e))

        return True

    def on_error(self, status):
        if status == 420:
            # Returning False if rate limit occurs
            return False
        print(status)


# This is the main function
if __name__ == "__main__":
    hash_tag_list = ['Microsoft', 'Bill Gates', 'Satya Nadella', 'Windows', 'Microsoft 365']
    fetched_tweets_filename = "tweets.json"
    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)
