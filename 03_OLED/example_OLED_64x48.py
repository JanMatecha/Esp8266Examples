from machine import I2C, Pin
from ssd1306 import *
import time

i2c = I2C(scl=Pin(5), sda=Pin(4))
oled = SSD1306_I2C(64, 48, i2c)

#vse vyplnit nicim - vymazat display
oled.fill(0)

#obdelnik
oled.rect(5, 5, 59, 43, 1)

#text
oled.text("Hello", 10, 20, 1)

#vyplneny obdelnik
oled.fill_rect(10, 30, 15, 10, 1)

#horizontalni cara
oled.hline(30, 30, 25, 1)

#vertikalni cara
oled.vline(30, 40, 10, 1)

#cara
oled.line(30, 40, 55, 35, 1)

#zobrazit na display
oled.show()

for n in range(5):
    time.sleep(5)
    #posun bufferu
    oled.scroll(5, 0)
    oled.show()

for n in range(5):
    time.sleep(5)
    #posun bufferu
    oled.scroll(-5, 0)
    oled.show()