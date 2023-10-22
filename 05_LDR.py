import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
ldr=18 #Measure the resistance of LDR and use ~ 1.5 times less its resistor value and connect that resistor to GPIO18 & Ground
GPIO.setup(ldr, GPIO.IN)

while True:
    if(GPIO.input(ldr)==1):
        print("LIGHT Detected....!")
    else:
        print("Watching...")
    time.sleep(0.5)
