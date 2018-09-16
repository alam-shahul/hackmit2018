import spotipy as sp
import spotipy.util as util

from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials()
SP = sp.Spotify(client_credentials_manager=client_credentials_manager)

hype_features = ['energy', 'danceability']
chill_features = ['acousticness', 'instrumentalness']

def sort_songs_by_feature(track_list):
	features = []
	for song_num in range(0, len(track_list), 50):
		features += SP.audio_features(track_list[song_num:song_num + 50])
	zip(track_list, features)
	hypeness = {}
	chillness = {}
	overall_hype_score = {}
	for track, feat in zip(track_list, features):
		hypeness[track] = sum([feat[x] for x in hype_features]) / 2.
		chillness[track] = sum([feat[x] for x in chill_features]) / 2.
		overall_hype_score[track] = hypeness[track] - chillness[track]
	return overall_hype_score

def find_closest_songs_to_rating(track_list, hype, chill, limit = 10):
	overall_hype = hype - chill
	hype_scores = sort_songs_by_feature(track_list)
	hype_dict = [{'track': k, 'hype_score': hype_scores[k]} for k in hype_scores]
	sorted_hype = sorted(hype_dict, key=lambda k: (k['hype_score'] - overall_hype) ** 2)
	return [t['track'] for t in sorted_hype][:limit]

def sort_songs_by_ratings(track_list, limit=10):
	with open('weights.txt', 'r') as f:
		num = float(f.read())
		hype = num - 0.5
		chill = 0.5 - num
		return find_closest_songs_to_rating(track_list, hype, chill, limit)

