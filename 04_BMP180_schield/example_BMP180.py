from machine import I2C, Pin
from bmp180 import BMP180

i2c = I2C(scl=Pin(5), sda=Pin(4))
bmp180 = BMP180(i2c)
bmp180.oversample_sett = 2
bmp180.baseline = 101325

print("Temperature is %s\u00b0C" % bmp180.temperature)
print("Presure is %sPa " % bmp180.pressure)
