import os
import logging
import csv
import tweepy

from actors import get_actors
from tweets import get_actor_tweets

logger = logging.getLogger('crawler_logger')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(logging.Formatter('%(levelname)s: %(asctime)s - %(message)s'))
logger.addHandler(ch)

BEARER_TOKEN = os.environ.get('bearer_token')

if __name__ == "__main__":
    logger.info('Starting Crawler')
    client = tweepy.Client(bearer_token=BEARER_TOKEN, wait_on_rate_limit=True)   
   
    logger.info("Getting Actors")
    actors = get_actors(client, 'data/accounts copy.csv')

    logger.info("Creating File")
    with open('data/tweets.csv', 'w', encoding="utf-8-sig") as tweets_file:
        field_names = [
            'id', 
            'actor_id',
            'actor_username',
            'withheld', 
            'created_at', 
            'harvested_at', 
            'conversation_id', 
            'lang', 
            'like_count', 
            'retweet_count', 
            'reply_count', 
            'quote_count', 
            'text', 
            'spectrum'
        ]
        csv_writer = csv.DictWriter(tweets_file, fieldnames=field_names, delimiter=';', quoting=csv.QUOTE_ALL)
        csv_writer.writeheader()
        for actor in actors:
            for tweet in get_actor_tweets(client, actor):
                csv_writer.writerow(dict(tweet))
            
        logging.debug('Finished')
