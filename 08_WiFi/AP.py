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
ip = '192.168.1.10'
subnet = '255.255.255.0'
gateway = '192.168.1.1'
dns = '8.8.8.8'
ap_if.ifconfig((ip,subnet,gateway,dns))
# kontrola nastaveni AP
print('network config:', ap_if.ifconfig())
# nastaveni AP
ESSID = "AP"
PASSWORD = "micropythoN"
AUTHMODE = network.AUTH_WPA_WPA2_PSK # 4 #network.AUTH_WEP
CHANNEL = 1
# ap_if.config(essid=ESSID, password=PASSWORD, authmode=, channel=CHANNEL)
ap_if.config(essid=ESSID, password=PASSWORD, authmode=AUTHMODE, channel=CHANNEL)

# kontrola nastaveni
print("essid:", ap_if.config('essid'))
print("channel:", ap_if.config('channel'))
print("authmode:", ap_if.config('authmode'))


