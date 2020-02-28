import os
import subprocess as sp
import csv

WLAN_SNR=sp.getoutput('iwconfig wlan0 | grep Rate | awk \'{print$2\'}')
WLAN_SIGNAL=sp.getoutput('iwconfig wlan0 | grep Quality | awk \'{print$4\'}')
WLAN_IP=sp.getoutput('ifconfig wlan0 | grep mask | awk \'{print$2\'}')

with open('SENSOR.csv', 'w', newline='') as csvfile:
    PRINTER = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    PRINTER.writerow([WLAN_IP] + [WLAN_SNR] + [WLAN_SIGNAL])

