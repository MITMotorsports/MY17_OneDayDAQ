#!/bin/bash
echo "Installing necessary packages..."
sudo apt update
sudo apt install cmake make gcc g++
echo "Packages installed!"

echo "Building WiringPi..."
/home/pi/wiringPi/build
echo "WiringPi built!"

echo "Building shutdownSwitch..."
/home/pi/shutdownSwitch/compile.sh
echo "shutdownSwitch built!"

echo "Building InertialSense cltool..."
cd /home/pi/InertialSenseSDK/InertialSenseCLTool
mkdir build
cd build
cmake ..
make
sudo usermod -a -G dialout $USER
sudo usermod -a -G plugdev $USER
echo "InertialSense cltool built!"

echo "Building candump..."
cd /home/pi/can-utils
make candump
make install || echo "It is okay that this failed!"
echo "candump built!"

echo "Setting up crontab..."
echo "@reboot /home/pi/startup.sh" | crontab -
echo "crontab set!"
