import numpy as np
import cv2, time

frame_counter=0
video = cv2.VideoCapture(0)

while(True):
    wasRead, frame = video.read()

    # operate on frame here
    print(frame.shape)
    cv2.imwrite("sample_frames/frame_%d.jpg" % frame_counter, frame)
    
    # Display frame
    cv2.imshow("Capturing", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    frame_counter += 1

video.release()
cv2.destroyAllWindows()
