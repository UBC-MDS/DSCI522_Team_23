############################################################
# Dockerfile to build wine_quality_prediction images
# Based on Ubuntu
############################################################

#Set base image to Ubuntu
FROM selenium/standalone-chrome

#Update repositor source list
RUN sudo apt-get update

################## BEGIN INSTALLATION ######################
#Install python basics
RUN sudo apt-get -y install \
    build-essential \
    python-dev \
    python-setuptools

# Create Timezon Variable
ENV DEBIAN_FRONTEND=noninteractive

# Install tzdata
RUN sudo apt-get install -y tzdata

# Install python pip
RUN sudo apt-get -y install python3-pip

RUN sudo apt-get -y install git-all
