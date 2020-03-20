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
        print("MERGE FAILED. SKIPPING\n\n#################################################")


def WLAN_SERVER_CONNECTOR():
    print("O) TRYING TO TRANSMIT FILE TO THE COLLECTOR SERVER")
    try:
        WLAN_CONNECTOR.WLAN_SCP()
        print("----CONNECTION SUCCESSFUL!")
        print("O) CLEANING JSON FILES\n\n#################################################")
        sp.getoutput('rm /home/pi/wlan_sensor/client/WLAN_PASSIVE/DATABASE/*.*')
    except:
        print("----CONNECTION FAILED. SKIPPING\n\n#################################################")


if __name__ == '__main__':

  while True:
    print("\n\n#################################################\n\nO) COLLECTING WLAN INFORMATION FROM THE OS. PLEASE WAIT 60s")

    i = 1
    while i < 16:
        WLAN_INFO.WLAN_PROCESS()
        time.sleep(4)
        print("---- COLLECTED "+str(i)+"/15")
        i +=1

    WLAN_SERVER_MERGE()

