# cam.py
# this is from https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
import numpy as np
import cv2
import time
import paho.mqtt.client as mqtt

LOCAL_MQTT_HOST="localhost"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="test_topic"

def on_connect_local(client, userdata, flags, rc):
        print("connected to local broker with rc: " + str(rc))

local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
# the index depends on your camera setup and which one is your USB camera.
# you may need to change to 1 or 2 depending on your machine.
cap = cv2.VideoCapture(0) # with macOS and an iphone, this might be your iphone camera
f = open("faces.txt", "a")
end = time.time() + 20
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
        print("publishing: ", msg)
        local_mqttclient.publish(LOCAL_MQTT_TOPIC,msg)
        cropped.append(png)
    
    f.write(cropped)
    # Display the resulting frame
    # cv2.imshow('frame',gray)

f.close()
    
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
