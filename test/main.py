import utime
from machine import Signal, Pin

led = Signal(Pin(2, Pin.OUT), invert=True)

while True:
    led.off()
    utime.sleep(1)
    led.on()
    utime.sleep(1)
