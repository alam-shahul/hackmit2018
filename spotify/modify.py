import spotipy
import spotipy.util as util

from BASIC_INFO import *

from SECRETS import OAUTH_TOKEN_SELF

def add_tracks_to_playlist(tracks):
	sp = spotipy.Spotify(auth=OAUTH_TOKEN_SELF)
	sp.trace = False
	results = sp.user_playlist_add_tracks(MY_USERNAME, 
										  PARTY_PLAYLIST, 
										  [tracks] if type(tracks) is not list else tracks)
	return (results)

def remove_tracks_from_playlist(tracks):
	sp = spotipy.Spotify(auth=OAUTH_TOKEN_SELF)
	sp.trace = False
	results = sp.user_playlist_remove_all_occurrences_of_tracks(MY_USERNAME, 
																PARTY_PLAYLIST, 
																[tracks] if type(tracks) is not list else tracks)
	return (results)
