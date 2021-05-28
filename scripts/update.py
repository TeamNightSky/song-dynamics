import os
from os.path import join
import requests
# from github import Github


RESTBASE = 'https://play.asti.ga/rest/'
PARAMS = {
    'u': os.getenv('EMAIL'),
    'p': os.getenv('PASSWORD'),
    't': os.getenv('TOKEN'),
    'v': '1.16.0',
    'c': 'Random-Song-Getter',
    'f': 'json'
}

song_resp = requests.get(
    join(RESTBASE, 'getRandomSongs'),
    params=dict(
        **PARAMS,
        size='1'
    )
)

song = song_resp.json()['subsonic-response']['randomSongs']['song'][0]

