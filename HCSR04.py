import time
from machine import Pin
Trig, Echo = Pin(16, Pin.OUT), Pin(14, Pin.IN)
Trig.value(0)
Echo.value(0)


async def chkdist():
    Trig.value(1)
    time.sleep(0.00001)
    Trig.value(0)
    while (Echo.value() == 0):
        pass
    t1 = time.ticks_us()
    while (Echo.value() == 1):
        pass
    t2 = time.ticks_us()
    t3 = time.ticks_diff(t2, t1)/8000
    return t3*340/2
