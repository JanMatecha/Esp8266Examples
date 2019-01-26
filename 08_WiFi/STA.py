# nastaveni stanice (station - STA)  a pripojeni k routeru
import network
sta_if = network.WLAN(network.STA_IF)
# kontrola zda je aktivni
sta_if.active()

# zapnuti STA
sta_if.active(True)
# nastaveni pripojeni
essid = "A"
password = "000AABB87DA6C"
sta_if.connect(essid, password)
# kotrola zda je stanice pripojena
sta_if.isconnected()
# kontrola nastaveni
sta_if.ifconfig()
# vypnuti STA
ap_if.active(False)
