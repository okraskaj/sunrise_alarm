import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
RED = 11
GREEN = 13
BLUE = 15
GPIO.setup(RED,GPIO.OUT)
GPIO.output(RED,0)
GPIO.setup(GREEN,GPIO.OUT)
GPIO.output(GREEN,0)
GPIO.setup(BLUE,GPIO.OUT)
GPIO.output(BLUE,0)

while (True):
    for col in [RED,GREEN,BLUE]:
        GPIO.output(col, 1)
        time.sleep(1)
        GPIO.output(col, 0)
