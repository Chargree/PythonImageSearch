import numpy as np
import cv2
import cherrypy


cap = cv2.VideoCapture(0)

print("This is the camera code: {}.").format(cap)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    grayed = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    # Display the resulting frame (press 'q' to end)
    cv2.imshow('frame',grayed)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyqAllWindows()