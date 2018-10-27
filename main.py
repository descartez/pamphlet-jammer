import network
import ujson
import usocket as socket

# opens up config file
f = open("config.json", "r")
configs = f.read()
config = ujson.loads(configs)
print(config)
f.close()

# sets up local network using config.json
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=config['essid_name'], authmode=int(config['authtype']))

if int(config['authtype']) != 0:
    ap.config(password=config['essid_password'])