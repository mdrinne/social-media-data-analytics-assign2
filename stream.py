#!/usr/bin/env python

#-----------------------------------------------------------------------
# twitter-stream-format:
#  - ultra-real-time stream of twitter's public timeline.
#    does some fancy output formatting.
#-----------------------------------------------------------------------

from twitter import *
import re
import datetime
from datetime import timedelta


#-----------------------------------------------------------------------
# import a load of external features, for text display and date handling
# you will need the termcolor module:
#
# pip install termcolor
#-----------------------------------------------------------------------
from time import strftime
from textwrap import fill
from termcolor import colored
from email.utils import parsedate

#-----------------------------------------------------------------------
# load our API credentials
#-----------------------------------------------------------------------
import sys
sys.path.append(".")
import config

#-----------------------------------------------------------------------
# create twitter streaming API object
#-----------------------------------------------------------------------
def create_stream():
    auth = OAuth(config.access_key,
                config.access_secret,
                config.consumer_key,
                config.consumer_secret)
    stream = TwitterStream(auth = auth, secure = True)
    return stream

#-----------------------------------------------------------------------
# iterate over tweets matching this filter text
#-----------------------------------------------------------------------


# while datetime.datetime.now() != future:
def get_stream(stream):
    dt = datetime.datetime.now()
    future = dt + timedelta(minutes=10)
    # later = future.strftime("%H:%M:%S")

    tweets = []

    tweet_iter = stream.statuses.sample(language='en')

    for tweet in tweet_iter:
        tweets.append(tweet)
        if datetime.datetime.now() > future:
            return tweets, dt, future
