# 1Day DAQ
## Setup on the Raspberry Pi
- Get a Raspbian Stretch Lite installation on the Pi
- `cd /home/pi`
- `git clone --recursive https://github.com/MITMotorsports/MY17_OneDayDAQ.git .`
- `mv -v scripts/* .`
- `sudo ./setup.sh`
- Connect an LED to pin 3 (header 15) and ground (header 14)
- Connect a shutdown button to pin 1 (header 12) and 3.3v (header 1)
- Remap as needed in /home/pi/pins
