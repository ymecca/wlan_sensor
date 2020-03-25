import os
import subprocess as sp


def WLAN_SCP():
        WLAN_SERVER = sp.getoutput('avahi-resolve -4 --name wlan-server.local | awk \'{print $2}\'')
        sp.getoutput('scp -q -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null /home/pi/wlan_sensor/client/WLAN_PASSIVE/DATABASE/DATABASE_PASSIVE.json '+WLAN_SERVER+':/home/devnet/wlan_sensor/client/DATABASE_PASSIVE.json')

if __name__ == '__main__':
        WLAN_SCP()

