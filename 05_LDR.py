import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
ldr=18
GPIO.setup(ldr, GPIO.IN)

while True:
    if(GPIO.input(ldr)==1):
        print("LIGHT Detected....!")
    else:
        print("Watching...")
    time.sleep(0.5)
