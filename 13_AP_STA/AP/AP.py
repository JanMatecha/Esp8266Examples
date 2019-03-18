#vytvoreni a nastaveni pro access point (AP)
import network
ap_if = network.WLAN(network.AP_IF)

# zapnuti AP
ap_if.active(True)

# nastaveni AP
ip = '192.168.1.10'
subnet = '255.255.255.0'
gateway = '192.168.1.10'
dns = '208.67.222.222'
ap_if.ifconfig((ip, subnet, gateway, dns))

# kontrola nastaveni AP
print('network config:', ap_if.ifconfig())

# nastaveni AP
ESSID = "AP"
PASSWORD = "micropythoN"
AUTHMODE = network.AUTH_WPA_WPA2_PSK
CHANNEL = 1
# ap_if.config(essid=ESSID, password=PASSWORD, authmode=, channel=CHANNEL)
ap_if.config(essid=ESSID, password=PASSWORD, authmode=AUTHMODE, channel=CHANNEL)

# kontrola nastaveni
print("essid:", ap_if.config('essid'))
print("channel:", ap_if.config('channel'))
print("authmode:", ap_if.config('authmode'))

