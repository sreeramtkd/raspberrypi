import RPi.GPIO as gpio
from picamera import PiCamera
import time
import telepot
from telepot.loop import MessageLoop
bot=telepot.Bot('**********************YOUR API KEY******************')
user='' # your telegram userid, get it form userinfobot
pir=23
i=0
gpio.setmode(gpio.BCM)
gpio.setup(pir,gpio.IN)

while True:
	while gpio.input(pir):
		camera = PiCamera()
		while (i<=4):
			camera.capture('/home/pi/Desktop/image%s.jpg' % i)
			print("Capturing...",i)
			bot.sendPhoto(user, photo=open('/home/pi/Desktop/image%s.jpg' % i, 'rb'))
			time.sleep(1)
			i=i+1
		camera.close()
		i=0
		time.sleep(10)

#camera.start_recording('/home/pi/Desktop/video.h264')
#sleep(5)
#camera.stop_recording()


