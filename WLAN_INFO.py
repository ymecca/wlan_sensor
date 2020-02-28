import os
import subprocess

WLAN_SNR=os.system('iwconfig wlan0 | grep Rate | awk \'{print$2\'}')
WLAN_SIGNAL=os.system('iwconfig wlan0 | grep Quality | awk \'{print$4\'}')
WLAN_IP=os.system('ifconfig wlan0 | grep mask | awk \'{print$2\'}')

print (WLAN_IP WLAN_SIGNAL WLAN_SNR)
