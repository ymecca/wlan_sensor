import os
import subprocess as sp
import csv

WLAN_RATE = sp.getoutput('iwconfig wlan0 | grep Rate | awk \'{print$2\'}')
WLAN_SIGNAL = sp.getoutput('iwconfig wlan0 | grep Quality | awk \'{print$4\'}')
WLAN_IP = sp.getoutput('ifconfig wlan0 | grep mask | awk \'{print$2\'}')

WLAN_RATE = WLAN_RATE.replace("Rate=","")
WLAN_SIGNAL = WLAN_SIGNAL.replace("level=","")

with open('DATABASE.csv', 'w', newline='') as csvfile:
    PRINTER = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    PRINTER.writerow([WLAN_IP]+[WLAN_RATE]+[WLAN_SIGNAL])

