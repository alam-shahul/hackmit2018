import cv2, time

video = cv2.VideoCapture(0)

check, frame = video.read()

print(frame)

cv2.imshow("Capturing", frame)

cv2.waitKey()

video.release()
