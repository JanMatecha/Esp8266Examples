from machine import Pin
import time


def blink(number, pin):
    n = 0
    while n < number:
        pin.on()
        time.sleep(0.3)
        pin.off()
        time.sleep(0.3)
        n = n+1


led = Pin(2, Pin.OUT)
blink(5, led)
led.on()



