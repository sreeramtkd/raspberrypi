import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
pir=4
led=5
GPIO.setup(pir, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

while True:
    if(GPIO.input(pir)):
        print("Motion Detected !")
        GPIO.output(led,1)
    else:
        print("Watching...")
        GPIO.output(led,0)
    time.sleep(0.5)
