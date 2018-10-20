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

def rgb(r,g,b):
    RED.ChangeDutyCycle(r)
    GREEN.ChangeDutyCycle(g)
    RED.ChangeDutyCycle(b)


while (True):
    r = 0
    g = 0
    b = 20
    
    # transition to dim yellow
    for i in range(50):
        r = r + 2
        g = g + 1
        #b = b - 1
        rgb(r,g,b)
        time.sleep(0.5)
    
    # transition to red 
    for i in range(50):
        r = r + 2
        g = g + 1
        b = b + 1
        rgb(r,g,b)
        time.sleep(0.5)
    
