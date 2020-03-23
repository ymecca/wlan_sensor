import hashlib
import os
import subprocess as sp
import json
import time
import datetime


def WLAN_PROCESS_IPERF():

        #MANDATORY FIELDS
        WLAN_TIME = int(time.time())
        WLAN_HARDWARE_MAC = sp.getoutput('ifconfig wlan0 | grep ether | awk \'{print$2\'}')
        WLAN_IPV4 = sp.getoutput('ifconfig wlan0 | grep mask | awk \'{print$2\'}')

        #BASE COMMANDS
                ### DHCP TIME


        WLAN_DHCP_STATUS = sp.getoutput('sudo nmap --script broadcast-dhcp-discover  > .DHCP_CHECK.txt 2>&1 ; cat .DHCP_CHECK.txt | grep "DHCP Message Type:" | awk \'{print $5}\'')
        WLAN_DHCP_TIME = sp.getoutput('cat .DHCP_CHECK.txt | grep "Nmap done:" | awk \'{print $11}\' ; rm -rf .DHCP_CHECK.txt')

        if WLAN_DHCP_STATUS == 'DHCPOFFER':
            WLAN_DHCP_STATUS = '1'

        else:
             WLAN_DHCP_STATUS = '0'

        ### DNS TIMES
        WLAN_DNS_UOL = sp.getoutput('dig uol.com.br | grep "Query time:" | awk \'{print $4}\'')
        WLAN_DNS_CISCO = sp.getoutput('dig cisco.com | grep "Query time:" | awk \'{print $4}\'')
        WLAN_DNS_BBC = sp.getoutput('dig bbc.co.uk | grep "Query time:" | awk \'{print $4}\'')
        WLAN_DNS_GOOGLE = sp.getoutput('dig google.com | grep "Query time:" | awk \'{print $4}\'')

        ### HTTP TIMES
        WLAN_HTTP_UOL = sp.getoutput('curl -so /dev/null -w \'%{time_total}\n\' uol.com.br')
        WLAN_HTTP_CISCO = sp.getoutput('curl -so /dev/null -w \'%{time_total}\n\' cisco')
        WLAN_HTTP_BBC = sp.getoutput('curl -so /dev/null -w \'%{time_total}\n\' bbc.co.uk')
        WLAN_HTTP_GOOGLE = sp.getoutput('curl -so /dev/null -w \'%{time_total}\n\' google.com')

        ### ICMP TIMES
        WLAN_ICMP_UOL = sp.getoutput('ping www.uol.com.br -c 5 -q | grep rtt | awk \'{print $4}\' | cut -d \'/\' -f 2')
        WLAN_ICMP_CISCO = sp.getoutput('ping cisco.com -c 5 -q | grep rtt | awk \'{print $4}\' | cut -d \'/\' -f 2')
        WLAN_ICMP_BBC = sp.getoutput('ping bbc.co.uk -c 5 -q | grep rtt | awk \'{print $4}\' | cut -d \'/\' -f 2')
        WLAN_ICMP_GOOGLE = sp.getoutput('ping google.com -c 5 -q | grep rtt | awk \'{print $4}\' | cut -d \'/\' -f 2')


        #SPECIAL COMMANDS
        WLAN_SERVER = sp.getoutput('avahi-resolve -4 --name wlan-server.local | awk \'{print $2}\'')

        WLAN_IPERF_UPLOAD = sp.getoutput('iperf3 -c '+WLAN_SERVER+' -P 10 -i 5 -t 5 -f m | grep SUM | grep "receiver" | awk \'{print $6}\'')
        WLAN_IPERF_DOWNLOAD = sp.getoutput('iperf3 -c '+WLAN_SERVER+' -P 10 -i 5 -t 5 -R -f m | grep SUM | grep sender | awk \'{print $6}\'')

        WLAN_HASH =  (str(WLAN_TIME) + WLAN_HARDWARE_MAC)
        WLAN_SHA = hashlib.sha256(WLAN_HASH.encode())
        WLAN_ID = WLAN_SHA.hexdigest()

        WLAN_SPEEDTEST_UP = ''
        WLAN_SPEEDTEST_DOWN = ''
        WLAN_SPEEDTEST_RTT = ''

        WLAN_DATA = {
                'WLAN_ID': WLAN_ID,
                'WLAN_TIME': WLAN_TIME,
                'WLAN_HARDWARE_MAC': WLAN_HARDWARE_MAC,
                'WLAN_IPV4': WLAN_IPV4,
                'WLAN_DNS_UOL': int(float(WLAN_DNS_UOL)),
                'WLAN_DNS_CISCO': int(float(WLAN_DNS_CISCO)),
                'WLAN_DNS_BBC': int(float(WLAN_DNS_BBC)),
                'WLAN_DNS_GOOGLE': int(float(WLAN_DNS_GOOGLE)),
                'WLAN_ICMP_UOL': int(float(WLAN_ICMP_UOL)),
                'WLAN_ICMP_CISCO': int(float(WLAN_ICMP_CISCO)),
                'WLAN_ICMP_BBC': int(float(WLAN_ICMP_BBC)),
                'WLAN_ICMP_GOOGLE': int(float(WLAN_ICMP_GOOGLE)),
                'WLAN_HTTP_UOL': int(float(WLAN_HTTP_UOL) * 1000),
                'WLAN_HTTP_CISCO': int(float(WLAN_HTTP_CISCO) * 1000),
                'WLAN_HTTP_BBC': int(float(WLAN_HTTP_BBC) * 1000) ,
                'WLAN_HTTP_GOOGLE': int(float(WLAN_HTTP_GOOGLE) * 1000),
                'WLAN_DHCP_TIME': int(float(WLAN_DHCP_TIME) * 1000),
                'WLAN_DHCP_STATUS': int(float(WLAN_DHCP_STATUS)),
				'WLAN_SPEEDTEST_UP': WLAN_SPEEDTEST_UP,
				'WLAN_SPEEDTEST_DOWN': WLAN_SPEEDTEST_DOWN,
				'WLAN_SPEEDTEST_RTT': WLAN_SPEEDTEST_RTT,
                'WLAN_IPERF_UPLOAD': int(float(WLAN_IPERF_UPLOAD)),
                'WLAN_IPERF_DOWNLOAD': int(float(WLAN_IPERF_DOWNLOAD))
                }

        WLAN_TIME = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        WLAN_JSON_FILE = 'DATABASE_ACTIVE_'+WLAN_TIME+'.tempjson'

        with open('/home/pi/wlan_sensor/client/WLAN_ACTIVE/DATABASE/'+WLAN_JSON_FILE, 'w') as json_file:
                json.dump(WLAN_DATA, json_file, indent=4)

def WLAN_PROCESS_BASE():

        #MANDATORY FIELDS
        WLAN_TIME = int(time.time())
        WLAN_HARDWARE_MAC = sp.getoutput('ifconfig wlan0 | grep ether | awk \'{print$2\'}')
        WLAN_IPV4 = sp.getoutput('ifconfig wlan0 | grep mask | awk \'{print$2\'}')

        #BASE COMMANDS
        ### DHCP TIME


        WLAN_DHCP_STATUS = sp.getoutput('sudo nmap --script broadcast-dhcp-discover  > .DHCP_CHECK.txt 2>&1 ; cat .DHCP_CHECK.txt | grep "DHCP Message Type:" | awk \'{print $5}\'')
        WLAN_DHCP_TIME = sp.getoutput('cat .DHCP_CHECK.txt | grep "Nmap done:" | awk \'{print $11}\' ; rm -rf .DHCP_CHECK.txt')

        if WLAN_DHCP_STATUS == 'DHCPOFFER':
            WLAN_DHCP_STATUS = '1'

        else:
             WLAN_DHCP_STATUS = '0'

        ### DNS TIMES
        WLAN_DNS_UOL = sp.getoutput('dig uol.com.br | grep "Query time:" | awk \'{print $4}\'')
        WLAN_DNS_CISCO = sp.getoutput('dig cisco.com | grep "Query time:" | awk \'{print $4}\'')
        WLAN_DNS_BBC = sp.getoutput('dig bbc.co.uk | grep "Query time:" | awk \'{print $4}\'')
        WLAN_DNS_GOOGLE = sp.getoutput('dig google.com | grep "Query time:" | awk \'{print $4}\'')

        ### HTTP TIMES
        WLAN_HTTP_UOL = sp.getoutput('curl -so /dev/null -w \'%{time_total}\n\' uol.com.br')
        WLAN_HTTP_CISCO = sp.getoutput('curl -so /dev/null -w \'%{time_total}\n\' cisco')
        WLAN_HTTP_BBC = sp.getoutput('curl -so /dev/null -w \'%{time_total}\n\' bbc.co.uk')
        WLAN_HTTP_GOOGLE = sp.getoutput('curl -so /dev/null -w \'%{time_total}\n\' google.com')

        ### ICMP TIMES
        WLAN_ICMP_UOL = sp.getoutput('ping www.uol.com.br -c 5 -q | grep rtt | awk \'{print $4}\' | cut -d \'/\' -f 2')
        WLAN_ICMP_CISCO = sp.getoutput('ping cisco.com -c 5 -q | grep rtt | awk \'{print $4}\' | cut -d \'/\' -f 2')
        WLAN_ICMP_BBC = sp.getoutput('ping bbc.co.uk -c 5 -q | grep rtt | awk \'{print $4}\' | cut -d \'/\' -f 2')
        WLAN_ICMP_GOOGLE = sp.getoutput('ping google.com -c 5 -q | grep rtt | awk \'{print $4}\' | cut -d \'/\' -f 2')

        WLAN_HASH =  (str(WLAN_TIME) + WLAN_HARDWARE_MAC)
        WLAN_SHA = hashlib.sha256(WLAN_HASH.encode())
        WLAN_ID = WLAN_SHA.hexdigest()

        WLAN_IPERF_UPLOAD = ''
        WLAN_IPERF_DOWNLOAD = ''
		
        WLAN_SPEEDTEST_UP = ''
        WLAN_SPEEDTEST_DOWN = ''
        WLAN_SPEEDTEST_RTT = ''

        WLAN_DATA = {
                'WLAN_ID': WLAN_ID,
                'WLAN_TIME': WLAN_TIME,
                'WLAN_HARDWARE_MAC': WLAN_HARDWARE_MAC,
                'WLAN_IPV4': WLAN_IPV4,
                'WLAN_DNS_UOL': int(float(WLAN_DNS_UOL)),
                'WLAN_DNS_CISCO': int(float(WLAN_DNS_CISCO)),
                'WLAN_DNS_BBC': int(float(WLAN_DNS_BBC)),
                'WLAN_DNS_GOOGLE': int(float(WLAN_DNS_GOOGLE)),
                'WLAN_ICMP_UOL': int(float(WLAN_ICMP_UOL)),
                'WLAN_ICMP_CISCO': int(float(WLAN_ICMP_CISCO)),
                'WLAN_ICMP_BBC': int(float(WLAN_ICMP_BBC)),
                'WLAN_ICMP_GOOGLE': int(float(WLAN_ICMP_GOOGLE)),
                'WLAN_HTTP_UOL': int(float(WLAN_HTTP_UOL) * 1000),
                'WLAN_HTTP_CISCO': int(float(WLAN_HTTP_CISCO) * 1000),
                'WLAN_HTTP_BBC': int(float(WLAN_HTTP_BBC) * 1000),
                'WLAN_HTTP_GOOGLE': int(float(WLAN_HTTP_GOOGLE) * 1000),
                'WLAN_DHCP_TIME': int(float(WLAN_DHCP_TIME) * 1000),
                'WLAN_DHCP_STATUS': int(float(WLAN_DHCP_STATUS)),
				'WLAN_SPEEDTEST_UP': WLAN_SPEEDTEST_UP,
				'WLAN_SPEEDTEST_DOWN': WLAN_SPEEDTEST_DOWN,
				'WLAN_SPEEDTEST_RTT': WLAN_SPEEDTEST_RTT,
                'WLAN_IPERF_UPLOAD': WLAN_IPERF_UPLOAD,
                'WLAN_IPERF_DOWNLOAD': WLAN_IPERF_DOWNLOAD
                }

        WLAN_TIME = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        WLAN_JSON_FILE = 'DATABASE_ACTIVE_'+WLAN_TIME+'.tempjson'

        with open('/home/pi/wlan_sensor/client/WLAN_ACTIVE/DATABASE/'+WLAN_JSON_FILE, 'w') as json_file:
                json.dump(WLAN_DATA, json_file, indent=4)

if __name__ == '__main__':
       WLAN_PROCESS_IPERF()

