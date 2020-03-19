import hashlib
import os
import subprocess as sp
import json
import time
import datetime


def WLAN_PROCESS():

        WLAN_IPERF_UPLOAD = sp.getoutput('iperf3 -c 192.168.1.76 -P 10 -i 5 -t 5 -f m | grep SUM | grep "receiver" | awk \'{print $6}\'')
        WLAN_IPERF_DOWNLOAD = sp.getoutput('iperf3 -c 192.168.1.76 -P 10 -i 5 -t 5 -R -f m | grep SUM | grep sender | awk \'{print $6}\'')
        WLAN_HARDWARE_MAC = sp.getoutput('ifconfig wlan0 | grep ether | awk \'{print$2\'}')
        WLAN_TIME = int(time.time())
        WLAN_IPV4 = sp.getoutput('ifconfig wlan0 | grep mask | awk \'{print$2\'}')


        WLAN_HASH =  (str(WLAN_TIME) + WLAN_HARDWARE_MAC)
        WLAN_SHA = hashlib.sha256(WLAN_HASH.encode())
        WLAN_ID = WLAN_SHA.hexdigest()


        WLAN_DATA = {
                'WLAN_ID': WLAN_ID,
                'WLAN_TIME': WLAN_TIME,
                'WLAN_HARDWARE_MAC': WLAN_HARDWARE_MAC,
                'WLAN_IPV4': WLAN_IPV4,
                'WLAN_IPERF_UPLOAD': WLAN_IPERF_UPLOAD,
                'WLAN_IPERF_DOWNLOAD': WLAN_IPERF_DOWNLOAD
                }

        WLAN_TIME = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        WLAN_JSON_FILE = 'DATABASE_ACTIVE_'+WLAN_TIME+'.tempjson'

        with open('/home/pi/wlan_sensor/client/WLAN_ACTIVE/DATABASE/'+WLAN_JSON_FILE, 'w') as json_file:
                json.dump(WLAN_DATA, json_file, indent=4)


if __name__ == '__main__':
        WLAN_PROCESS()

