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
		while (i<=2):
			camera.capture('/home/pi/Desktop/image%s.jpg' % i)
			print("Capturing...",i)
			time.sleep(3)
			i=i+1
		camera.close()
		i=0
		time.sleep(10)

#camera.start_recording('/home/pi/Desktop/video.h264')
#sleep(5)
#camera.stop_recording()


