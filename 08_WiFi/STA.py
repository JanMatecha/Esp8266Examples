# nastaveni stanice (station - STA)  a pripojeni k routeru
import network
sta_if = network.WLAN(network.STA_IF)
# kontrola zda je aktivni
sta_if.active()

# zapnuti STA
sta_if.active(True)
# nacteni ESSID a Hesla ze souboru config.txt
f = open('config.txt')
essid = f.readline().rstrip("\n")
password = f.readline().rstrip("\n")
f.close()
# nastaveni pripojeni
sta_if.connect(essid, password)
# kotrola zda je stanice pripojena
sta_if.isconnected()
# kontrola nastaveni
sta_if.ifconfig()
# vypnuti STA
sta_if.active(False)
