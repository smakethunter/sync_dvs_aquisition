FROM ubuntu:22.04

#
# Python3.8 install for Ubuntu
#
COPY metavision.list .
RUN cp metavision.list /etc/apt/sources.list.d
# RUN add-apt-repository -y ppa:s-schmeisser/ogre-1.12
RUN apt-get update
RUN apt -y install libcanberra-gtk-module mesa-utils ffmpeg
RUN apt -y install cmake libboost-program-options-dev libeigen3-dev
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get install -y python3-pip
RUN apt-get install -y python3.10
RUN apt -y install python3.10-dev
# Update symlink to point to latest

RUN python3 --version
RUN pip3 --version

RUN apt-get update
#RUN apt -y install metavision-sdk

