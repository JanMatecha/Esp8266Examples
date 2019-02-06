#vytvoreni a nastaveni pro access point (AP)
import network
ap_if = network.WLAN(network.AP_IF)
# kontrola zda je aktivni
ap_if.active()
# kontrola nastaveni AP
ap_if.ifconfig()

# IP address, netmask, gateway, DNS
# priklad:
#   ('192.168.4.1', '255.255.255.0', '192.168.4.1', '8.8.8.8')


# zapnuti AP
ap_if.active(True)
# nastaveni AP
ESSID = "AP"
PASSWORD = "micropythoN"
# CHANNEL = 3
# ap_if.config(essid=ESSID, password=PASSWORD, authmode=network.AUTH_WEP, channel=CHANNEL)
# ap_if.config(essid=ESSID, password=PASSWORD, authmode=network.AUTH_WEP)
ap_if.config(essid=ESSID, password=PASSWORD, authmode=network.AUTH_WPA_WPA2_PSK)
# ap_if.config(essid="wemos", password="abcdabcdabcd", authmode=network.AUTH_WPA_WPA2_PSK)
print('network config:', ap_if.ifconfig())
# kontrola nastaveni AP
ap_if.ifconfig()
ip = '192.168.1.10'
subnet = '255.255.255.0'
gateway = '192.168.1.1'
dns = '8.8.8.8'
ap_if.ifconfig((ip,subnet,gateway,dns))
ap_if.ifconfig()


# Takhle zjistim defaultni nazev wifi
# https://github.com/micropython/micropython/blob/master/ports/esp8266/modules/inisetup.py
# import ubinascii
# ap_if = network.WLAN(network.AP_IF)
# essid = b"MicroPython-%s" % ubinascii.hexlify(ap_if.config("mac")[-3:])
# ap_if.config(essid=essid, authmode=network.AUTH_WPA_WPA2_PSK, password=b"micropythoN")


print(ap_if.config('essid'))
print(ap_if.config('channel'))

