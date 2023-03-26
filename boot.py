import network
import gc
import uos
import machine
import utime

ap_if = network.WLAN(network.AP_IF)
ap_if.active(True)
ap_if.config(essid="ESP-CAR")
ap_if.config(password="12345678")
while ap_if.active() == False:
    pass

gc.collect()
print("IP Address:"+ap_if.ifconfig()[0])


