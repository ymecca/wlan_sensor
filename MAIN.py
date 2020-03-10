import time
import WLAN_INFO
import WLAN_CONNECTOR
import os
import subprocess as sp

while True:
    print("Gathering WLAN Information from OS")


    i = 0
    while i < 6:
        WLAN_INFO.WLAN_PROCESS()
        time.sleep(1)
        print(i)
        i +=1

    print("Transmit file to the Collector Server")
    WLAN_CONNECTOR.WLAN_SCP()
    print("Cleaning CSV File")
    sp.getoutput('cat /home/pi/wlan_sensor/client/DATABASE/DATABASE.csv')
    #sp.getoutput('rm -rf /home/pi/wlan_sensor/client/DATABASE/DATABASE.csv')
    print("Countdown 5sec...")
    time.sleep(5)
