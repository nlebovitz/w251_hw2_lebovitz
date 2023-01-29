FROM alpine:latest
RUN apk add mosquitto
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools
RUN pip3 install paho-mqtt
# Configure to allow remote access
RUN echo "allow_anonymous true" > /etc/mosquitto/mosquitto.conf
RUN echo "listener 1883 0.0.0.0" >> /etc/mosquitto/mosquitto.conf
CMD ["mosquitto","-c","/etc/mosquitto/mosquitto.conf"]
COPY "forward.py" .
CMD ["python3","forward.py"]
