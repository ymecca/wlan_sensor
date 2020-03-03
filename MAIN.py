import time
import WLAN_INFO
import WLAN_CONNECTOR

while True:
    print("Gathering WLAN Information from OS")
    WLAN_INFO
    print("Transmit file to the Collector Server")
    WLAN_CONNECTOR
    print("Countdown 5sec...")
    time.sleep(5)
