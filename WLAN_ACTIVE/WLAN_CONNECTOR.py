import os
import subprocess as sp


def WLAN_SCP():
        WLAN_SERVER = sp.getoutput('cat /home/pi/wlan_sensor/client/WLAN_SERVER.txt')
        sp.getoutput('scp -q -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null /home/pi/wlan_sensor/client/WLAN_ACTIVE/DATABASE/DATABASE_ACTIVE.json '+WLAN_SERVER+':/home/devnet/wlan_sensor/client/DATABASE_ACTIVE.json')

if __name__ == '__main__':
        WLAN_SCP()


