import spotipy
import spotipy.util as util

from BASIC_INFO import *

from SECRETS import OAUTH_TOKEN_SELF

def add_tracks_to_playlist(tracks):
	sp = spotipy.Spotify(auth=OAUTH_TOKEN_SELF)
	sp.trace = False
	results = sp.user_playlist_add_tracks(MY_USERNAME, PARTY_PLAYLIST, track_ids)
	return (results)