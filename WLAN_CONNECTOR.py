from paramiko import SSHClient
from scp import SCPClient

ssh = SSHClient()
ssh.load_system_host_keys()
ssh.connect('192.168.1.86')

# SCPCLient takes a paramiko transport as an argument
scp = SCPClient(ssh.get_transport())

scp.put('/home/pi/wlan_sensor/client/DATABASE/DATABASE.json', '/home/devnet/wlan_sensor/client/')
