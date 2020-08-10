#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tweepy
from tweepy import OAuthHandler, Stream


# In[ ]:


from tweepy.streaming import StreamListener
import socket
import json


# In[ ]:


cosumer_key = '6a6O3uc45EsVQizvpOe9vLb7n'
consumer_secret = 'IuF1iTrZWA23223yB4Dynfjh4ZG0tM9zUGl5iopyohbO10J2JL'
access_token = '872997408808075265-gRbrN9id9ddhcTN3NiAag6UNtHBHaTF'
access_secret= '3hGwXw7UN0yf43qE1bV2qn7f4eYKuic4fedlm8sKtgZUi'


# In[ ]:


class TweetListener(StreamListener):
    def __init__(self, csocket):
        self.client_socket = csocket
        
    def on_data(self, data):
        try:
            msg = json.loads(data)
            print(msg['text'].encode('uft-8'))
            self.client_socket.send(msg['text'].encode('utf-8'))
            return True
        except BaseException as e:
            print("Error" , e)
        return True
    
    def on_error(self, status):
        print(status)
        return True


# In[ ]:


def sendData(c_socket):
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    
    twitter_stream = Stream(auth, TweetListener(c_socket))
    twitter_stream.filter(track=['guitar'])


# In[ ]:


if __name__ == "__main__":
    s = socket.socket()
    host = '127.0.0.1'
    port = 5555
    s.bind((host,port))
    print('listening on port 5555')
    s.listen(5)
    c,addr = s.accept()
    sendData(c)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




