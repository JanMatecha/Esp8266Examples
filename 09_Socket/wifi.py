
def do_connect(config_file="config.py"):
    f = open(config_file)
    essid = f.readline().rstrip("\r\n")
    password = f.readline().rstrip("\r\n")
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


def do_disconnect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(False)


def ip_address():
    import network
    sta_if = network.WLAN(network.STA_IF)
    return sta_if.ifconfig()[0]


