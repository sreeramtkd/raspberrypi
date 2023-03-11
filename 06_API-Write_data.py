import requests
import time
import Adafruit_DHT as dht
while True:
    humidity,temperature=dht.read_retry(dht.DHT11,4)
    requests.get('https://api.thingspeak.com/update?api_key=AJG9J825FVJDSQG2&field1='+str(temperature)+'field2='+str(humidity))
    time.sleep(60)
