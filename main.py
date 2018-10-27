import network
import time
import usocket as socket
import ure
import ujson

# opens up config file
f = open("config.json", "r")
configs = f.read()
config = ujson.loads(configs)
print(config)
f.close()

# sets up local network using config.json
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=config['essid_name'])
ap.config(authmode=int(config['authmode_int']))

if int(config['authmode_int']) != 0:
    print("auth required, setting password")
    ap.config(password=config['essid_password'])

