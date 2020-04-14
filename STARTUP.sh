#!/bin/bash

echo -ne "\n\n#####################################\nEnter WLAN Server IP or DNS name:  "
read WLAN_SERVER
echo $WLAN_SERVER > /home/pi/wlan_sensor/client/WLAN_SERVER.txt
echo -e "#####################################\n"

source /home/pi/environment/wlan_sensor/bin/activate
nohup python -u /home/pi/wlan_sensor/client/WLAN_PASSIVE/MAIN.py > /home/pi/wlan_sensor/client/WLAN_PASSIVE/LOG/LOGFILE.log &
nohup python -u /home/pi/wlan_sensor/client/WLAN_ACTIVE/MAIN.py > /home/pi/wlan_sensor/client/WLAN_ACTIVE/LOG/LOGFILE.log &

echo -e "DONE"
