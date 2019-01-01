import dht
import time
from machine import I2C, Pin
sensor = dht.DHT22(Pin(2))

sensor.measure()

print("T = %s\u00b0C" % sensor.temperature())
print("H = %s%%" % sensor.humidity())
n = 0
while True:
    time.sleep(5)
    n += 1
    retry = 0
    while retry < 3:
        try:
            sensor.measure()
            break
        except:
            retry = retry + 1
            print(".", end="")
    print("\n**********************")
    print("N = %s " % n)
    print("T = %s\u00b0C" % sensor.temperature())
    print("H = %s%%" % sensor.humidity())

