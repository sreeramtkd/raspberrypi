import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
LED=[5,6,13,19,26]
GPIO.setup(LED, GPIO.OUT,initial=0)

while True:
    for i in range(len(LED)):
        GPIO.output(LED[i],GPIO.HIGH)
        time.sleep(.5)
        GPIO.output(LED[i],GPIO.LOW)
        time.sleep(.5)
