import os
import re

import tweepy


CONSUMER_KEY = os.environ['TWITTER_API_KEY']
CONSUMER_SECRET = os.environ['TWITTER_API_SECRET_KEY']
ACCESS_KEY = os.environ['TWITTER_ACCESS_TOKEN']
ACCESS_SECRET = os.environ['TWITTER_ACCESS_TOKEN_SECRET']

RT_RE = re.compile('^RT @\w+: ')
URL_RE = re.compile('http.*?(\s|$)')


def clean_tweet(txt: str) -> str:
    """Remove:
       - RT @...
       - links
    """
    txt = maybe_rm_rt(txt)
    txt = maybe_rm_urls(txt)
    return txt


def maybe_rm_rt(txt: str) -> str:
    if txt.startswith('RT @'):
        return RT_RE.sub('', txt)
    return txt


def maybe_rm_urls(txt: str) -> str:
    if 'http' in txt:
        return URL_RE.sub('', txt)
    return txt


def print_some_tweets():
    """Just for playing around."""
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    api = tweepy.API(auth)

    number_of_tweets = 50
    tweets = api.home_timeline(count=number_of_tweets)
    print('\n\n'.join([clean_tweet(tweet.text) for tweet in tweets]))


if __name__ == '__main__':
    print_some_tweets()

    # tweets = get_tweets()
    #     for t in tweets:
    #         if fits_meter(t):
    #             retweet(t)
