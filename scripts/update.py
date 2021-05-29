import os
from os.path import join
import requests
import datetime
from github import Github

SHIFT = 5
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
now = datetime.datetime.now()

title = song.get('title')
author = song.get('artist', 'Not listed')
timestamp = "{}:{:02}:{:02}".format(
    (now.hour + 24 - SHIFT) % 24,
    now.minute,
    now.second
)

with open('scripts/template.html', 'r') as f:
    template = f.read()


g = Github(os.getenv('PAT'))
repo = g.get_repo('GrandMoff100/song-dynamics')

contents = repo.get_contents('index.html')
repo.update_file(
    contents.path, 
    f"Updated song website at {timestamp}", 
    template % (timestamp, title, author), 
    contents.sha, 
    branch="master"
)

