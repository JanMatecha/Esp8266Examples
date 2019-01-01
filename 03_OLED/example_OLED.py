from machine import I2C, Pin
from ssd1306 import *
import time

i2c = I2C(scl=Pin(5), sda=Pin(4))
oled = SSD1306_I2C(128, 64, i2c)

#vse vyplnit nicim - vymazat display
oled.fill(0)

#obdelnik
oled.rect(5, 5, 123, 59, 1)

#text
oled.text("Hello World", 25, 20, 1)

#vyplneny obdelnik
oled.fill_rect(100, 45, 15, 10, 1)

#horizontalni cara
oled.hline(10, 50, 25, 1)

#vertikalni cara
oled.vline(10, 45, 10, 1)

#cara
oled.line(15, 45, 25, 35, 1)

#zobrazit na display
oled.show()

for n in range(5):
    time.sleep(5)
    #posun bufferu
    oled.scroll(20, 0)
    oled.show()
