from hcsr04 import HCSR04
from machine import I2C, Pin
from ssd1306 import *
import time

i2c = I2C(scl=Pin(5), sda=Pin(4))
oled = SSD1306_I2C(128, 64, i2c)

sensor = HCSR04(trigger_pin=14, echo_pin=12)

while True:
    time.sleep(1)
    oled.fill_rect(0, 0, 128, 64, 0)
    try:
        distance = sensor.distance_cm()
        print('Distance:', distance, 'cm')
    except OSError as ex:
        print('ERROR getting distance:', ex)
    oled.text("D = %scm" % distance, 1, 1, 1)
    print('Distance:', distance, 'cm')
    oled.show()
