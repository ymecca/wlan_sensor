from paramiko import SSHClient
from scp import SCPClient
import os
import subprocess as sp


def WLAN_SCP():
        WLAN_SERVER = sp.getoutput('avahi-resolve -4 --name wlan-server.local | awk \'{print $2}\'')
        ssh = SSHClient()
        ssh.load_system_host_keys()
        ssh.connect(WLAN_SERVER)
        # SCPCLient takes a paramiko transport as an argument
        scp = SCPClient(ssh.get_transport())
        scp.put('/home/pi/wlan_sensor/client/WLAN_PASSIVE/DATABASE/DATABASE_PASSIVE.json', '/home/devnet/wlan_sensor/client/DATABASE_PASSIVE.json')
        scp.close()

if __name__ == '__main__':
        WLAN_SCP()

