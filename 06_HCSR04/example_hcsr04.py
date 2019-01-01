from hcsr04 import HCSR04
import time

sensor = HCSR04(trigger_pin=16, echo_pin=0, echo_timeout_us=1000000)
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
