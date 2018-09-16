import face_recognition
import numpy as np
import cv2

def custom_compare_faces(known_face_encodings, face_encoding_to_check, tolerance=0.6):
    distances=face_recognition.face_distance(known_face_encodings, face_encoding_to_check)
    index=np.argmin(distances)
    if distances[index] <= tolerance:
        return index
    return None

def get_spotify_ids(img, encoding_to_spotify_id):
    """
    img is given as a numpy 2D array
    output is a list of spotify IDs
    """
    # get list of known faces as encodings
    known_faces = list(encoding_to_spotify_id.keys())

    # make a list of spotify IDs of the people in the image
    spotify_ids = []

    # get encoding of every person in the image
    for encoding in face_recognition.face_encodings(img):
        #results = face_recognition.compare_faces(known_faces, encoding)
        match_index = custom_compare_faces(known_faces, encoding)

        if match_index is not None:
            match_encoding=known_faces[match_index]
            spotify_ids.append(encoding_to_spotify_id[match_encoding])

        #for i, face_found in enumerate(results):
        #    if not face_found:
        #        continue
        #    encoding = known_faces[i]
        #    spotify_ids.append(encoding_to_spotify_id[encoding])


    return list(set(spotify_ids))


if __name__=="__main__":
    #img = cv2.imread("facial_recognition_test_images/yeet.jpg")
    #img = cv2.imread("facial_recognition_test_images/mahi_and_shahul_test.jpg")
    img = cv2.imread("facial_recognition_test_images/squad2.jpg")
    ids = get_spotify_ids(img, image_to_spotify_id)
    print(ids)



