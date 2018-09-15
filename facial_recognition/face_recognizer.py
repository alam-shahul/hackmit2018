import face_recognition

# Load the jpg files into numpy arrays
andy_image = face_recognition.load_image_file("../face_images/andy.jpg")
shahul_image = face_recognition.load_image_file("../face_images/shahul.jpg")
jingyu_image = face_recognition.load_image_file("../face_images/jingyu.jpg")
mahi_image = face_recognition.load_image_file("../face_images/mahi.jpg")


# List spotify ID's
andy_spotify = "12129338584?si=fJghDTmuSZegUk7z1KULkA"
shahul_spotify = "fuck me daddy"
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
    import numpy as np
    import cv2
    #img = cv2.imread("facial_recognition_test_images/yeet.jpg")
    #img = cv2.imread("facial_recognition_test_images/mahi_and_shahul_test.jpg")
    img = cv2.imread("facial_recognition_test_images/squad2.jpg")
    ids = get_spotify_ids(img, image_to_spotify_id)
    print(ids)



