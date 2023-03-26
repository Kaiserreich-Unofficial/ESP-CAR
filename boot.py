import network
import gc
import uos
import machine
import utime

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.scan()
sta_if.connect("tjuwlan", "")

gc.collect()
utime.sleep_ms(1000)
print("IP Address:"+sta_if.ifconfig()[0])
