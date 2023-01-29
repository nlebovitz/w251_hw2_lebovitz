FROM ubuntu
  
RUN apt-get update
RUN apt install -y python3-pip
RUN pip3 install paho-mqtt
RUN pip3 install Cython
RUN pip3 install numpy
# example from https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
COPY "cam.py" .
CMD ["python3","cam.py"]
