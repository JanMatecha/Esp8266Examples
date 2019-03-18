# nastaveni stanice (station - STA)  a pripojeni k routeru
import network
sta_if = network.WLAN(network.STA_IF)
# zapnuti STA
sta_if.active(True)
ESSID = "AP"
PASSWORD = "micropythoN"

# nastaveni pripojeni
sta_if.connect(ESSID, PASSWORD)
# kotrola zda je stanice pripojena
sta_if.isconnected()
# kontrola nastaveni
sta_if.ifconfig()
# nastavine staticke IP adresy
a = sta_if.ifconfig()
b = list(a)
b[0] = '192.168.1.12'
c = tuple(b)
sta_if.ifconfig(c)
# kontrola nastaveni
sta_if.ifconfig()
