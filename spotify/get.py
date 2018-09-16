import spotipy as sp
import spotipy.util as util

from spotipy.oauth2 import SpotifyClientCredentials

from BASIC_INFO import *


client_credentials_manager = SpotifyClientCredentials()
SP = sp.Spotify(client_credentials_manager=client_credentials_manager)

def get_playlists(user_id):
    playlists = SP.user_playlists(user_id)
    if 'items' in playlists:
        return [pl['uri'].split(':')[-1] for pl in playlists['items']]
    return []

def get_songs_from_playlist(user_id, playlist_id):
    playlist_tracks = SP.user_playlist_tracks(user_id, playlist_id, fields='items,uri,name,id,total', market='fr')
    if 'items' in playlist_tracks:
        return [pl['track']['id'] for pl in playlist_tracks['items']]
    return []

def get_all_songs(user_id):
    playlists = get_playlists(user_id)
    songs = []
    for pl in playlists:
        songs += get_songs_from_playlist(user_id, pl)
    return songs

def reset_playlist(user_id, playlist_id):
    songs = get_songs_from_playlist(user_id, playlist_id)

if __name__=="__main__":
    USER_ID = '22zrcabx54xzpwfktbhgok3nq'
    print(get_all_songs(USER_ID))


