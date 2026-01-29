from wifi import conecta
import dht
import machine
import time
import urequests

sensor = dht.DHT11(machine.Pin(4))
rele = machine.Pin(2, machine.Pin.OUT)

station = conecta()
if station.isconnected():
    print("Conectado ao wifi")
else:
    print("Falha na conexao wifi")

def thingspeak(temperatura, umidade):
    url = f"https://api.thingspeak.com/update?api_key=EWZAIPF6ZF67TRGL&field1={temperatura}&field2={umidade}"
    
    response = urequests.get(url)
    print("Dados enviados ao ThingSpeak, Resposta:", response.text)
    response.close()

while True:
    sensor.measure()
    temp = sensor.temperature()
    umid = sensor.humidity()

    print("temp={}, Umid={}".format(temp, umid))
    
    if temp > 31 or umid > 70:
        rele.value(1)
        thingspeak(temp, umid)
    else:
        rele.value(0)

    time.sleep(15)

# station.disconnect()