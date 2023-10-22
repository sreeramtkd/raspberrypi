import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
pir=23
GPIO.setup(pir, GPIO.IN)

while True:
    if(GPIO.input(pir)):
        print("Motion Detected !")
    else:
        print("Watching...")
    time.sleep(0.5)
