from typing import Dict

import csv
import string
import re

from nltk.tokenize import TweetTokenizer

EMOJI_LEXICONS_PATH = './preprocessing/lexicons/emoji_utf8_lexicon_ptbr.txt'
EMOJI_LEXICONS_TRANSLATOR = {}

with open(EMOJI_LEXICONS_PATH, 'r', encoding="utf-8-sig") as emoji_file:
    csv_reader = csv.DictReader(emoji_file, delimiter='\t')
    for row in csv_reader:
        EMOJI_LEXICONS_TRANSLATOR[row['emoji']] = row['text']

def remove_retweet(token: str) -> str: 
    if token.lower()=='rt':
        return ''
    return token

def remove_hashtags(token: str) -> str: 
    if '#' in token:
        return ''
    return token

def remove_punctuation(token: str) -> str: 
    if token in string.punctuation:
        if token in ',.!?':
            return token
        return ''
    return token

def remove_url(token: str) -> str:
    return re.sub(r'^https?:\/\/.*[\r\n]*', '', token, flags=re.MULTILINE)

def remove_emoji(token: str, emoji_translator: Dict[str, str]) -> str:
    if token in emoji_translator.keys():
        return re.sub(token, emoji_translator[token], token, flags=re.MULTILINE)

    return token

def preprocess_token(token: str) -> str:
    token = remove_retweet(token)
    token = remove_hashtags(token)
    token = remove_punctuation(token)
    token = remove_url(token)
    token = remove_emoji(token, EMOJI_LEXICONS_TRANSLATOR)

    return token

def preprocessing(tweet: str, tokenizer: TweetTokenizer) -> str:
    return ' '.join([preprocess_token(token) for token in tokenizer.tokenize(tweet)]).strip()
