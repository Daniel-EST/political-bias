from typing import Iterator
import csv

import tweepy


class Actor:
    def __init__(self, username: str, spectrum: str, id: int, banned: bool = False):
        self.__username = username
        self.__spectrum = spectrum
        self.__id = id

    @property
    def username(self) -> str:
        return self.__username
    
    @property
    def spectrum(self) ->  str:
        return self.__spectrum

    @property
    def id(self) -> int:
        return self.__id

    def __str__(self):
        return f"{self.__class__.__name__}(username='@{self.__username}', user_id={self.__id}, spectrum='{self.__spectrum})"

def get_actor_user_id(username: str, client: tweepy.Client) -> int:
    user = client.get_user(username=username)
    return user.data.id

def get_actors(client: tweepy.Client, file_path: str = 'data/accounts.csv') -> Iterator[Actor]:
    with open(file_path, 'r', encoding="utf-8-sig") as actors_file:
        csv_reader = csv.DictReader(actors_file, delimiter=';')
        for row in csv_reader:
            username = row['username']
            spectrum = row['spectrum']
            user_id = get_actor_user_id(row['username'], client)
            yield Actor(username, spectrum, user_id)
