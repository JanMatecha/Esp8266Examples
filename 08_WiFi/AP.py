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

