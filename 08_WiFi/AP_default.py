#vytvoreni a nastaveni pro access point (AP)
import network
ap_if = network.WLAN(network.AP_IF)
# kontrola zda je aktivni
ap_if.active()
# zapnuti AP
ap_if.active(True)

# kontrola nastaveni AP
ap_if.ifconfig()
# nastaveni AP
ip = '192.168.4.1'
subnet = '255.255.255.0'
gateway = '192.168.4.1'
dns = '208.67.222.222' # OpenDNS
ap_if.ifconfig((ip,subnet,gateway,dns))
# kontrola nastaveni AP
print('network config:', ap_if.ifconfig())




# https://github.com/micropython/micropython/blob/master/ports/esp8266/modules/inisetup.py
import ubinascii
ESSID = b"MicroPython-%s" % ubinascii.hexlify(ap_if.config("mac")[-3:])
PASSWORD = "micropythoN"
AUTHMODE = network.AUTH_WPA_WPA2_PSK
CHANNEL = 1
ap_if.config(essid=ESSID, password=PASSWORD, authmode=AUTHMODE, channel=CHANNEL)
# kontrola nastaveni
print("essid:", ap_if.config('essid'))
print("channel:", ap_if.config('channel'))
print("authmode:", ap_if.config('authmode'))







