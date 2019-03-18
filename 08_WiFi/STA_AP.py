# nastaveni stanice (station - STA)  a pripojeni k Wemos
import network
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
ESSID = "AP"
PASSWORD = "micropythoN"

sta_if.connect(ESSID, PASSWORD)
# kotrola zda je stanice pripojena
sta_if.isconnected()
# kontrola nastaveni
sta_if.ifconfig()

