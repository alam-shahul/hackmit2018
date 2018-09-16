import spotipy as sp
import spotipy.util as util

from spotipy.oauth2 import SpotifyClientCredentials

import ui

client_credentials_manager = SpotifyClientCredentials()
SP = sp.Spotify(client_credentials_manager=client_credentials_manager)

def sort_songs_by_feature(track_list, feature='danceability'):
	features = []
	for song_num in range(0, len(track_list), 50):
		features += SP.audio_features(track_list[song_num:song_num + 50])
	zip(track_list, features)
	print(features)
