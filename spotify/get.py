import spotipy as sp
import spotipy.util as util
from BASIC_INFO import *
from SECRETS import OAUTH_TOKEN_SELF

import requests

SP = sp.Spotify(auth=OAUTH_TOKEN_SELF)

def get_playlists(user_id):
    return SP.user_playlists(user_id)

def get_songs_from_playlist(user_id, playlist_id):
    playlist_tracks = SP.user_playlist_tracks(user_id, playlist_id, fields='items,uri,name,id,total', market='fr')

def get_all_songs(user_id):
    playlists = get_playlists(user_id)
    songs = []
    for pl in playlist:
        songs += get_songs_from_playlist(user_id, pl)
    return songs

USER_ID = '22zrcabx54xzpwfktbhgok3nq'
print(get_all_songs(USER_ID))


