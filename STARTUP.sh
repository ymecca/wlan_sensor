#!/bin/bash

source /home/pi/environment/wlan_sensor/bin/activate
nohup python -u /home/pi/wlan_sensor/client/MAIN.py > /home/pi/wlan_sensor/client/LOG/LOGFILE.log &
