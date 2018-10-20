import RPi.GPIO as GPIO
import time


rpin = 23
gpin = 24
bpin = 25
freq = 100
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(rpin, GPIO.OUT)
GPIO.setup(gpin, GPIO.OUT)
GPIO.setup(bpin, GPIO.OUT)
RED = GPIO.PWM(rpin, freq)
RED.start(0)
GREEN = GPIO.PWM(gpin, freq)
GREEN.start(0)
BLUE = GPIO.PWM(bpin, freq)
BLUE.start(0)
frequency = freq
while (True):
    for col in [RED, GREEN, BLUE]:
        for i in range(100):
            col.ChangeDutyCycle(i)
        col.ChangeDutyCycle(2)