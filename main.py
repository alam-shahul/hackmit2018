import sys, os
sys.path.insert(0, os.path.abspath('..'))
import requests
from spotify.get import *
from spotify.modify import *

if __name__=="__main__":
    user_id = sys.argv[1]
    songs=get_all_songs(user_id)
    add_tracks_to_playlist(songs)
    remove_tracks_from_playlist(songs)   
    print("done!")
