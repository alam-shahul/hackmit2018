import spotipy
import spotipy.util as util

from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def sort_songs_by_feature(track_list, feature='danceability'):
	features = []
	for song_num in range(0, len(track_list), 50):
		features += spotipy.audio_features(track_list[song_num:song_num + 50])
	print features