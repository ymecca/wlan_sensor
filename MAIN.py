import time
import WLAN_INFO
import WLAN_CONNECTOR
import WLAN_JSON_MERGE
import os
import subprocess as sp


def WLAN_SERVER_CONNECTOR():
    print("TRYING TO TRANSMIT FILE TO THE COLLECTOR SERVER")
    try:
        WLAN_CONNECTOR.WLAN_SCP()
        print("----CONNECTION SUCCESSFUL!")
        print("CLEANING JSON FILES\n\n#################################################")
        sp.getoutput('rm /home/pi/wlan_sensor/client/DATABASE/*.*')
    except:
        print("CONNECTION FAILED. SKIPPING\n\n#################################################")

while True:
    print("\n\n#################################################\n\nCOLLECTING WLAN INFORMATION FROM THE OS. PLEASE WAIT 60s")

    i = 1
    while i < 16:
        WLAN_INFO.WLAN_PROCESS()
        time.sleep(4)
        print("---- COLLECTED "+str(i)+"/15")
        i +=1

    print("MERGING JSON FILES")
    WLAN_JSON_MERGE.WLAN_MERGE()
    WLAN_SERVER_CONNECTOR()    
