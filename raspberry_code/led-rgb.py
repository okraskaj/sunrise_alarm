import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
RED = 23
GREEN = 24
BLUE = 25
GPIO.setup(RED,GPIO.OUT)
GPIO.output(RED,0)
GPIO.setup(GREEN,GPIO.OUT)
GPIO.output(GREEN,0)
GPIO.setup(BLUE,GPIO.OUT)
GPIO.output(BLUE,0)

while (True):
    for col in [RED,GREEN,BLUE]:
        GPIO.output(col, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(col, GPIO.LOW)
