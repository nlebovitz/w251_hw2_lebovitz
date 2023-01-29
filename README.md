W251 HW 2 Lebovitz
S3 storage: https://nlebovitz-hw2.s3.amazonaws.com/faces.txt

10 points for explaining the MQTT topics and the QoS that you used:
MQTT topics:
I used the structure that was listed in the lab. I had a broker on the edge and also in the cloud running in a container and a k8s service containing the container on each platform. I had the face detector app set up as a publisher which sent messages on localhost to the forwarder. The forwarder container had a listener and a publisher listening on local host and publishing to the EC2 cloud. In the cloud I had the other broker opening the MQTT service with a listener in the processor container to process the image text files and send them to S3.

QoS topics:
I did not use QoS as much as I should have because it was difficult to implement in the time allotted. I did attempt to build in queining and policing by iterating through the messages and policing by sending responses for each message published.

Cloud EC2 structure:
2 containers
  1) broker
  2) listener
