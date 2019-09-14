#!/bin/bash

pkill -f /home/pi/SenseHatPatterns/control.py
cd /home/pi/SenseHatPatterns/deploy/
./killall.sh
python3 /home/pi/SenseHatPatterns/sensehat/misc/matrix_clear.py
