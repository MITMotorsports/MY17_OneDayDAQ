#!/bin/bash
DIRE="/home/pi"
${DIRE}/shutdownSwitch/shutdownSwitch &

# Configure status LED
LED=$(cat ${DIRE}/pins/led.pin)
gpio mode ${LED} OUTPUT
gpio write ${LED} 1

sleep 2

# Enable and start CAN Logging
sudo /sbin/ip link set can0 up type can bitrate 500000
cd ${DIRE}/CAN_logs
candump -l any,0:0,#FFFFFFFF 2>> ${DIRE}/logoflogs &

# Start INS Logging
/home/pi/InertialSenseSDK/InertialSenseCLTool/build/cltool -sINS1 -sINS2 -sDualIMU -sIMU1 -sIMU2 -sGPS -sMag1 -sBaro -sSensors -sDThetaVel -c="/dev/ttyUSB0" -lp="/home/pi/INS_logs" &

# Blink
gpio blink ${LED} &

exit 0
