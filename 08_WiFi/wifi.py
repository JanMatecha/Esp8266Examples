
def do_connect(config_file = "config.txt"):
    f = open(config_file)
    essid = f.readline().rstrip("\n")
    password = f.readline().rstrip("\n")
    f.close()

    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(essid, password)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

