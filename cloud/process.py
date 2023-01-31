import paho.mqtt.client as mqtt
import boto3
import numpy as np
import cv2

s3 = boto3.client('s3')
bucket_name = 'nlebovitz-hw2'
bucket = s3.get_bucket(bucket_name)
LOCAL_MQTT_HOST="localhost"
LOCAL_MQTT_PORT=30250
LOCAL_MQTT_TOPIC="test_topic"

def on_connect_local(client, userdata, flags, rc):
        print("connected to local broker with rc: " + str(rc))
        client.subscribe(LOCAL_MQTT_TOPIC)
	
def on_message(client,userdata, msg):
  try:
    print("message received: ",str(msg.payload.decode("utf-8")))
    buff = np.fromstring(msg.payload, np.uint8)
    buff = buff.reshape(1, -1)
    img = cv2.imdecode(buff, cv2.IMREAD_COLOR)
    s3.upload_file(img, bucket)

  except:
    print("Unexpected error:", sys.exc_info()[0])

local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
local_mqttclient.on_message = on_message



# go into a loop
local_mqttclient.loop_forever()
