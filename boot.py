import network
import gc
import uos
import machine
import utime

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid="ESP-CAR", password="123456")

gc.collect()
utime.sleep_ms(1000)
print("IP Address:"+ap.ifconfig()[0])
