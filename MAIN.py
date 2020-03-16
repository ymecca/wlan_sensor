import time
import WLAN_INFO
import WLAN_CONNECTOR
import WLAN_JSON_MERGE
import os
import subprocess as sp

while True:
    print("Gathering WLAN Information from OS")


    i = 0
    while i < 15:
        WLAN_INFO.WLAN_PROCESS()
        time.sleep(4)
        print(i)
        i +=1
    
    print("Merging JSON Files")
    WLAN_JSON_MERGE.WLAN_MERGE() 
    print("Transmit file to the Collector Server")
    WLAN_CONNECTOR.WLAN_SCP()
    print("Cleaning JSON Files")
    sp.getoutput('rm /home/pi/wlan_sensor/client/DATABASE/*.*')   
