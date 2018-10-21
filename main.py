import network
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid='Free Resources')
ap.config(authmode=3, password='123456789')