from typing import Iterator, Dict
import tweepy
from datetime import datetime, timezone

from actors import Actor


class Tweet:
    def __init__(self,
                 id: int,
                 actor: Actor,
                 withheld: bool,
                 created_at: str,
                 harvested_at: str,
                 conversation_id: int,
                 lang: str,
                 text: str,
                 public_metrics: Dict[str, int],
                 ):
        self.__id = id
        self.__actor = actor
        self.__withheld = withheld
        self.__created_at = created_at
        self.__harvested_at = harvested_at
        self.__conversation_id = conversation_id
        self.__lang = lang
        self.__text = text
        self.__public_metrics = public_metrics

    @property
    def id(self) -> int:
        return self.__id

    @property
    def actor(self) -> Actor:
        return self.__actor

    @property
    def withheld(self) -> str:
        return self.__withheld

    @property
    def created_at(self) -> str:
        return self.__created_at

    @property
    def harvested_at(self) -> str:
        return self.__harvested_at

    @property
    def conversation_id(self) -> str:
        return self.__conversation_id

    @property
    def lang(self) -> str:
        return self.__lang

    @property
    def text(self) -> str:
        return self.__text

    @property
    def public_metrics(self) -> str:
        return self.__public_metrics

    def __str__(self):
        return f"{self.__class__.__name__}(id='@{self.__id}', text={self.__text}, actor='{self.__actor})"

    def __iter__(self):
        yield 'id', self.__id
        yield 'actor_id', self.__actor.id
        yield 'actor_username', self.__actor.username
        yield 'withheld', self.__withheld
        yield 'created_at', self.__created_at
        yield 'harvested_at', self.__harvested_at
        yield 'conversation_id', self.__conversation_id
        yield 'text', self.__text
        yield 'like_count', self.__public_metrics['like_count']
        yield 'retweet_count', self.__public_metrics['retweet_count']
        yield 'reply_count', self.__public_metrics['reply_count']
        yield 'quote_count',  self.__public_metrics['quote_count']
        yield 'lang', self.__lang
        yield 'spectrum', self.__actor.spectrum


def get_actor_tweets(client: tweepy.Client, actor: Actor) -> Iterator[Tweet]:
    tweets = tweepy.Paginator(
        client.get_users_tweets, actor.id,
        tweet_fields=['created_at', 'public_metrics', 'lang', 'author_id',
                      'conversation_id', 'context_annotations', 'withheld'],
        max_results=100, limit=40
    ).flatten()
    for tweet in tweets:
        withheld = tweet.withheld != None
        harvested_at = datetime.now(
            timezone.utc).strftime("%Y-%m-%d %H:%M:%S%z")
        harvested_at = f'{harvested_at[0:-2]}:{harvested_at[-2:]}'
        yield Tweet(
            tweet.id,
            actor,
            withheld,
            tweet.created_at,
            harvested_at,
            tweet.conversation_id,
            tweet.lang,
            tweet.text,
            tweet.public_metrics
        )
