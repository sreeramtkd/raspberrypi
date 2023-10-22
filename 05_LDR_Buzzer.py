import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
pir=18
GPIO.setup(pir, GPIO.IN)

while True:
    if(!GPIO.input(pir)):
        print("Watching....!")
    else:
        print("LIGHT Detected...")
    time.sleep(0.5)
