import glob


def WLAN_MERGE():

    WLAN_READ_JSON = glob.glob("/home/pi/wlan_sensor/client/WLAN_ACTIVE/DATABASE/*.tempjson")
    with open ("/home/pi/wlan_sensor/client/WLAN_ACTIVE/DATABASE/DATABASE_ACTIVE.json", "w") as jsonfile:
        jsonfile.write('[{}]'.format(
            ','.join([open(f, "r").read() for f in WLAN_READ_JSON])))

if __name__ == '__main__':
        WLAN_MERGE()

