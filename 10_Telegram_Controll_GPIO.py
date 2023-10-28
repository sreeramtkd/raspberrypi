# sudo pip install telepot telegram
from datetime import datetime
import time
import telepot
import RPi.GPIO as GPIO
import Adafruit_DHT as dht
from telepot.loop import MessageLoop
#Connect DHT11 to pin 4

GPIO.setmode(GPIO.BCM)
LED=[26,19,13,6,5]
GPIO.setup(LED, GPIO.OUT,initial=0)

def on(pin):
    GPIO.output(pin,GPIO.HIGH)
    return

def off(pin):
    GPIO.output(pin,GPIO.LOW)
    return

def th():
    humidity,temperature = dht.read_retry(dht.DHT11, 4)
    humidity = round(humidity, 2)
    temperature = round(temperature, 2)
    return temperature,humidity

bot = telepot.Bot('*********************YOUR BOT API KEY******************')

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    #if you want to allow access only from a certain user enable the below line and use intentaion for the rest of the LOCs untill MessageLoop, To get your telegram ID use underinfobot
    #if(msg['from']['id']==************):
    if(msg['text'] == '/on'):
        on(5)
        state = GPIO.input(5)
        if(state==1):
            bot.sendMessage(chat_id, "LED Is Turned ON")
        else:
            bot.sendMessage(chat_id, "An Error Occured...")
    if(msg['text'] == '/off'):
        off(5)
        state = GPIO.input(5)
        if(state==0):
            bot.sendMessage(chat_id, "LED Is Turned OFF")
        else:
            bot.sendMessage(chat_id, "An Error Occured...")
    if('username' in msg['from']):
        print(msg['from']['username'], " Sent msg",msg['text']," ")
    else:
        print(msg['text'])
    if(msg['text'] == '/dht'):
        r=th()
        bot.sendMessage(chat_id, "Temp: "+str(r[0]))
        bot.sendMessage(chat_id, "Humd: "+str(r[1]))

MessageLoop(bot, handle).run_as_thread()

