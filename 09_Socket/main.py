import wifi
wifi.do_connect(config_file="config.py")
print("IP adresa je: %s" % wifi.ip_address())
wifi.do_disconnect()
