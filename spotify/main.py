import requests
import sys
from get import *
from modify import *

if __name__=="__main__":
    user_id = sys.argv[1]
    songs=get_all_songs(user_id)
    add_tracks_to_playlist(songs)
    
    print("done!")
