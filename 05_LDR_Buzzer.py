import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
pir=18
GPIO.setup(pir, GPIO.IN)

while True:
    if(GPIO.input(pir)==0):
        print("LIGHT Detected....!")
    else:
        print("Watching...")
    time.sleep(0.5)
