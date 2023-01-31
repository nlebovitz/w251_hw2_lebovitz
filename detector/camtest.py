# cam.py
# this is from https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
import numpy as np
import cv2
import time

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# the index depends on your camera setup and which one is your USB camera.
# you may need to change to 1 or 2 depending on your machine.
cap = cv2.VideoCapture(0) # with macOS and an iphone, this might be your iphone camera
f = open("faces.txt", "a")

count = 0
end = time.time() + 10
while(time.time() < end):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    cropped = []
    for (x,y,w,h) in faces:
        face = gray[y:y+h, x:x+h]
        rc, png = cv2.imencode('.png', face)
        msg = png.tobytes()
        f.write(str(msg))
        cv2.imwrite("frame%d.jpg" % count, face)
        count += 1
        print("publishing: ", msg)
        #local_mqttclient.publish(LOCAL_MQTT_TOPIC,msg)
        cropped.append(png)
    
    
    # Display the resulting frame
    # cv2.imshow('frame',gray)

f.close()
    
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
