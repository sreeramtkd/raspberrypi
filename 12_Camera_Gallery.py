import RPi.GPIO as gpio
from picamera import PiCamera
import time
pir=23
i=0
gpio.setmode(gpio.BCM)
gpio.setup(pir,gpio.IN)

while True:
	while gpio.input(pir):
		camera = PiCamera()
		camera.resolution = (800, 600)
		while (i<=4):
			camera.capture('/var/www/html/img/image%s.jpg' % i)
			print("Capturing...",i)
			time.sleep(.5)
			i=i+1
		camera.close()
		i=0
		time.sleep(10)
