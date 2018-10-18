#Importing necessary libraries

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Varibales that contains user credentials to access Twitter API
access_token = 'This contains your access token key'
access_token_secret = 'this contains your secret key'
consumer_key = 'This contains your consumer key'
consumer_secret = 'This contains your consumer secret key'

#This is the basic listener that prints out the tweets receivec to stdout

class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #This handles Twitter authentication and the connection to Twitter API Streaming
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filters Twitter Stream to capture data by the keywords microsoft, stock price
    stream.filter(track=['Microsoft', 'Stock Price'])








