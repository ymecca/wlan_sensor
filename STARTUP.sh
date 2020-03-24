#!/bin/bash

source /home/pi/environment/wlan_sensor/bin/activate
nohup python -u /home/pi/wlan_sensor/client/WLAN_PASSIVE/MAIN.py > /home/pi/wlan_sensor/client/WLAN_PASSIVE/LOG/LOGFILE.log &
nohup python -u /home/pi/wlan_sensor/client/WLAN_ACTIVE/MAIN.py > /home/pi/wlan_sensor/client/WLAN_ACTIVE/LOG/LOGFILE.log &
