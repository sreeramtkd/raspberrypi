#! sudo pip install Adafruit_DHT
import Adafruit_DHT as dht
import time
#Connect DHT11 to pin 4

while True:
  humidity,temperature = dht.read_retry(dht.DHT11, 4)
  print('T='+str(temperature)+' | H='+str(humidity))
  time.sleep(1)
