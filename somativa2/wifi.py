def conecta():
    ssid = "wifi_name"
    senha = "wifi_senha"

    import network
    import time
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssid, senha)
    for t in range(50):
        if station.isconnected():
            break
        time.sleep(0.1)
    return station