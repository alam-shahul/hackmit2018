import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

from BASIC_INFO import *

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

token = util.prompt_for_user_token(MY_USERNAME, 'playlist-modify-public')
if token:
    sp = spotipy.Spotify(auth=token)


def add_tracks_to_playlist(tracks):
	sp.trace = False
	results = sp.user_playlist_add_tracks(MY_USERNAME, 
										  PARTY_PLAYLIST, 
										  [tracks] if type(tracks) is not list else tracks)
	return (results)