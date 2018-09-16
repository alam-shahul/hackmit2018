import requests
import sys
from face_recognizer import *
from get import *
from modify import *

def load_defaults():
    # Load the jpg files into numpy arrays
    andy_image = face_recognition.load_image_file("../face_images/andy.jpg")
    shahul_image = face_recognition.load_image_file("../face_images/shahul.jpg")
    jingyu_image = face_recognition.load_image_file("../face_images/jingyu.jpg")
    mahi_image = face_recognition.load_image_file("../face_images/mahi.jpg")
    
    # List spotify ID's
    andy_spotify = "12129338584?si=fJghDTmuSZegUk7z1KULkA"
    shahul_spotify = "exme7663dhexz4c6sy72ekhpc"
    jingyu_spotify = "22zrcabx54xzpwfktbhgok3nq"
    mahi_spotify = "22di6xshcftebczzi7rdcd74y"
    
    # Make lists
    images = [andy_image, shahul_image, jingyu_image, mahi_image]
    spotifies = [andy_spotify, shahul_spotify, jingyu_spotify, mahi_spotify]
    
    # Create dictionary where 
    # keys = face encodings / feature vectors
    # values = spotify IDs

    image_to_spotify_id = dict()
    for i in range(len(images)):
        encoding = face_recognition.face_encodings(images[i])[0] # assumption: only 1 face in image
        image_to_spotify_id[tuple(encoding)] = spotifies[i]

    return image_to_spotify_id

def process_frame(frame, image_to_spotify_id, current_tracks, users_to_songs, users_to_countdowns):
    user_ids = get_spotify_ids(frame, image_to_spotify_id)
    print(user_ids)
    tracks_to_add=set()
    tracks_to_remove=set()
     
    for user_id in user_ids:
        if user_id == MY_USERNAME:
            continue

        users_to_countdowns[user_id] = 30
        #new_tracks = set(get_all_songs(user_id))
        new_tracks = set(get_sorted_songs(user_id))

        if len(new_tracks) ==0:
            raise ValueError()
        print("New tracks?", new_tracks)

        if user_id in users_to_songs:
            old_songs = set(users_to_songs[user_id]) - new_tracks
            tracks_to_remove.update(old_songs)

        users_to_songs[user_id] = list(new_tracks)

        tracks_to_add.update(new_tracks)

    current_tracks.difference_update(tracks_to_remove)
    tracks_to_add = tracks_to_add - current_tracks
    current_tracks.update(tracks_to_add)

    print("Current tracks", current_tracks)
    print("Removing", tracks_to_remove)
    print("Adding", tracks_to_add)

    remove_tracks_from_playlist(list(tracks_to_remove))
    add_tracks_to_playlist(list(tracks_to_add))

    return tracks_to_add

if __name__=="__main__":
    reset_playlist()

    from time import time, sleep

    users_to_songs={}
    users_to_countdowns={}
    playlist_tracks=set(get_songs_from_playlist(MY_USERNAME, PARTY_PLAYLIST))
    frame_counter=0

    video = cv2.VideoCapture(0)

    while(True):
        wasRead, frame = video.read()
    
        # operate on frame here
        print(frame.shape)
    
        # Display frame
        cv2.imshow("Capturing", frame)

        added_tracks = process_frame(frame, image_to_spotify_id, playlist_tracks, users_to_songs, users_to_countdowns)
        print(users_to_songs)

        current_users=list(users_to_countdowns.keys())

        for user in current_users:
            users_to_countdowns[user] -= 1
            if users_to_countdowns[user] <= 0:
                remove_tracks_from_playlist(users_to_songs[user])
                del users_to_countdowns[user]

        print(users_to_countdowns)   

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
        frame_counter += 1
    
    video.release()
    reset_playlist()
    cv2.destroyAllWindows()


    ##image_to_spotify_id = load_defaults()
    ###img = cv2.imread("../face_images/jingyu.jpg")
    ###img = cv2.imread("facial_recognition_test_images/squad2.jpg")
    ##img = cv2.imread("../face_images/mahi.jpg")
    ##h,w,_ = img.shape
    ###img=cv2.resize(img, (w//2, h//2))
    ##cv2.imshow("test", img)
    ##cv2.waitKey(0)
    ##x = time()
    ##playlist_tracks=set(get_songs_from_playlist(MY_USERNAME, PARTY_PLAYLIST))
    ##added_tracks = process_frame(img, image_to_spotify_id, playlist_tracks)
    ##print(time() - x, 'seconds for processing frame')
    ##x = time()
    ##playlist_tracks.update(added_tracks)
    ##print(time() - x, 'seconds for adding tracks')
    ##
    ###remove_tracks_from_playlist(list(playlist_tracks))   
    ###reset_playlist()
    
    print("done!")
