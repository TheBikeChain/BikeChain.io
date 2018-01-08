#!/bin/bash
# ------------------------------------------------------------------
# [Michael Free] The Bikechain
#          Install Depenedencies for running the Bikechain dev app
#          in a linux environment
#
#          http://bikechain.io
#
# Built for Ubuntu 16.04.*     
# ------------------------------------------------------------------
# update ubuntu environment
apt-get update
# install OS dependencies
apt-get install -y python3 python3-pip git python3-setuptools python3-pygame python3-opengl python3-gst0.10 python3-enchant gstreamer0.10-plugins-good python3-dev build-essential python3-pip libgl1-mesa-dev libgles2-mesa-dev zlib1g-dev ffmpeg
# add new repositority
add-apt-repository ppa:mc3man/trusty-media
apt-get update
pip3 install pygments docutils
# Make sure Pip, Virtualenv and Setuptools are updated
pip3 install --upgrade pip3 virtualenv setuptools
virtualenv --no-site-packages kivyinstall
. kivyinstall/bin/activate
pip3 install git+https://github.com/kivy/kivy.git@master
