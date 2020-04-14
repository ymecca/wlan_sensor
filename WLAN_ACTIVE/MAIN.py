import time
import WLAN_INFO
import WLAN_CONNECTOR
import WLAN_JSON_MERGE
import os
import subprocess as sp

def WLAN_SERVER_MERGE():
    print("O) TRYING TO MERGE THE JSON FILES")
    try:
        WLAN_JSON_MERGE.WLAN_MERGE()
        print("----MERGED SUCCESSFULLY!")
        WLAN_SERVER_CONNECTOR()
    except:
        print("MERGE FAILED. SKIPPING")


def WLAN_SERVER_CONNECTOR():
    print("O) TRYING TO TRANSMIT FILE TO THE COLLECTOR SERVER")
    try:
        WLAN_CONNECTOR.WLAN_SCP()
        print("----CONNECTION SUCCESSFUL!")
        print("O) CLEANING JSON FILES")
        sp.getoutput('rm /home/pi/wlan_sensor/client/WLAN_ACTIVE/DATABASE/*.*')
    except:
        print("----CONNECTION FAILED. SKIPPING")


if __name__ == '__main__':

  while True:
    print("\n\n#################################################\n\nO) STARTING ACTIVE COLLECTING INFORMATIONS FROM THE OS. PLEASE WAIT!" )

    i = 0
    while i < 20:
        WLAN_INFO.WLAN_PROCESS_BASE()
        i +=1
        print("---- COLLECTED BASE "+str(i)+"/20")


    i = 0
    while i < 1:
        WLAN_INFO.WLAN_PROCESS_IPERF()
        i +=1
        print("---- COLLECTED IPERF "+str(i)+"/1")


    WLAN_SERVER_MERGE()
    print("COUNTDOWN 1800s\n\n#################################################")
    time.sleep(10)

