import spotipy as sp
import spotipy.util as util

from spotipy.oauth2 import SpotifyClientCredentials

from BASIC_INFO import *


client_credentials_manager = SpotifyClientCredentials()
SP = sp.Spotify(client_credentials_manager=client_credentials_manager)

def get_playlists(user_id):
    return SP.user_playlists(user_id)

def get_songs_from_playlist(user_id, playlist_id):
    playlist_tracks = SP.user_playlist_tracks(user_id, playlist_id, fields='items,uri,name,id,total', market='fr')
    return playlist_tracks

def get_all_songs(user_id):
    playlists = get_playlists(user_id)
    print (playlists)
    songs = []
    for pl in playlists:
        print (pl)    	
        songs += get_songs_from_playlist(user_id, pl)
    return songs

USER_ID = '22zrcabx54xzpwfktbhgok3nq'
print(get_all_songs(USER_ID))


