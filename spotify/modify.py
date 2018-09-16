import spotipy
from get import *
import spotipy.util as util

from BASIC_INFO import *

AUTH_TOKEN = util.prompt_for_user_token(MY_USERNAME, 'playlist-modify-public')
if AUTH_TOKEN:
    sp = spotipy.Spotify(auth=AUTH_TOKEN)
else:
    raise ValueError("Cannot authenticate to your account")

def add_tracks_to_playlist(tracks):
    sp.trace = False

    if not tracks:
        return None

    for idx in range(0, len(tracks), 100):
        results = sp.user_playlist_add_tracks(MY_USERNAME, 
                                              PARTY_PLAYLIST, 
                                              [tracks] if type(tracks) is not list else tracks[idx:idx+100])
    return (results)

def remove_tracks_from_playlist(tracks):
    sp.trace = False

    if not tracks:
        return None

    for idx in range(0, len(tracks), 100):
        results = sp.user_playlist_remove_all_occurrences_of_tracks(MY_USERNAME, 
                                                                    PARTY_PLAYLIST, 
                                                                    [tracks] if type(tracks) is not list else tracks[idx:idx+100])
    return (results)

def reset_playlist():
    songs = get_songs_from_playlist(MY_USERNAME, PARTY_PLAYLIST)
    remove_tracks_from_playlist(songs)
