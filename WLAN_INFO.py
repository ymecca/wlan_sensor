import os
import subprocess as sp
import json

WLAN_RATE = sp.getoutput('iwconfig wlan0 | grep Rate | awk \'{print$2\'}')
WLAN_SIGNAL = sp.getoutput('iwconfig wlan0 | grep Quality | awk \'{print$4\'}')
WLAN_IPV4 = sp.getoutput('ifconfig wlan0 | grep mask | awk \'{print$2\'}')
WLAN_TIME = sp.getoutput('date')

WLAN_RATE = WLAN_RATE.replace("Rate=","")
WLAN_SIGNAL = WLAN_SIGNAL.replace("level=","")
WLAN_TIME = WLAN_TIME.replace(" ","_")

DATA = {}
DATA['WLAN'] = []
DATA['WLAN'].append({
    'WLAN_RATE(Mbps)': WLAN_RATE,
    'WLAN_SIGNAL(dBM)': WLAN_SIGNAL,
    'WLAN_IPV4': WLAN_IPV4,
    'WLAN_TIME': WLAN_TIME

})

with open('DATABASE.json', 'w') as outfile:
    json.dump(DATA, outfile)
