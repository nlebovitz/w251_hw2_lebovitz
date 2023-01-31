W251 HW 2 Lebovitz
S3 storage: https://nlebovitz-hw2.s3.amazonaws.com/faces.txt

10 points for explaining the MQTT topics and the QoS that you used:
MQTT topics:
I used the structure that was listed in the lab. I had a broker on the edge and also in the cloud running in a container and a k8s service containing the container on each platform. I kept the topic as "test topic" because I knew that had worked for me in the lab and kept the same structure in the cloud. All of my brokers, listeners, and publishers subscribed to "test-topic".

QoS topics:
I let MQTT keep QoS at a default of 0 which is 'best-effort' delivery. This was acceptable for my implementation because I can check the listener in the cloud on my own to see if the messages are coming through. If i implemented this for a real app I would want 1 or 2 to make sure I was getting receipt that the message was received. With QoS 2, it makes sure the message is receieved exactly once as well. This would be for more robust apps where you need to ensure the message was published and only once but for the sake of this app and my sanity I kept it at 0.

Edge Structure:
4 containers:
  1) broker
  2) detector (face detection py files with publisher)
  3) forwarder (listener and publishes to cloud)
  4) logger (listener which logs to bash)

Cloud EC2 structure:
2 containers
  1) broker
  2) listener
