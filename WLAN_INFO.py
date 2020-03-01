import os
import subprocess as sp
import json
import time

WLAN_RATE = sp.getoutput('iwconfig wlan0 | grep Rate | awk \'{print$2\'}')
WLAN_SIGNAL = sp.getoutput('iwconfig wlan0 | grep Quality | awk \'{print$4\'}')
WLAN_IPV4 = sp.getoutput('ifconfig wlan0 | grep mask | awk \'{print$2\'}')
WLAN_TIMESTAMP = time.time()
WLAN_HARDWARE_MAC = sp.getoutput('ifconfig wlan0 | grep ether | awk \'{print$2\'}')
WLAN_TX_POWER = sp.getoutput('iwconfig wlan0 | grep Rate | awk \'{print$4\'}')
WLAN_RETRIES = sp.getoutput('iwconfig wlan0 | grep "excessive retries" | awk \'{print$3\'}')

WLAN_TX_POWER = WLAN_TX_POWER.replace("Tx-Power=","")
WLAN_RATE = WLAN_RATE.replace("Rate=","")
WLAN_SIGNAL = WLAN_SIGNAL.replace("level=","")
WLAN_RETRIES = WLAN_RETRIES.replace("retries:","")

DATA = {}
DATA['WLAN'] = []
DATA['WLAN'].append({
    'WLAN_TIMESTAMP': WLAN_TIMESTAMP,
    'WLAN_HARDWARE_MAC': WLAN_HARDWARE_MAC,
    'WLAN_IPV4': WLAN_IPV4,
    'WLAN_RATE(Mbps)': WLAN_RATE,
    'WLAN_SIGNAL(dBm)': WLAN_SIGNAL,
    'WLAN_TX_POWER(dBm)': WLAN_TX_POWER

})

with open('DATABASE.json', 'w') as outfile:
    json.dump(DATA, outfile)


