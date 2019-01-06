from hcsr04 import HCSR04
import time

#TODO
# echo_pin=0 nefungovalo po nahrani na WEMOS, nerozbehlo se a nesel ani restart, s konsole fungovalo
# echo_pin=2 , ale sviti porad dioda na Wemosu
# , echo_timeout_us=1000000
# funkcni kombinace:  echo - GPIO12(D6), trigger - GPIO14 (D5)

sensor = HCSR04(trigger_pin=14, echo_pin=12)
distance = sensor.distance_cm()

print('Distance:', distance, 'cm')

n = 0
while True:
    time.sleep(1)
    try:
        distance = sensor.distance_cm()
        print('Distance:', distance, 'cm')
    except OSError as ex:
        print('ERROR getting distance:', ex)

    print('Distance:', distance, 'cm')
