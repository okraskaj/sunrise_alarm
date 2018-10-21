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


class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def get_centimal_vals(self):
        return (100 * self.r / 255,
                100 * self.g / 255,
                100 * self.b / 255
                )


def set_rgb(col):
    r, g, b = col.get_centimal_vals()
    RED.ChangeDutyCycle(r)
    GREEN.ChangeDutyCycle(g)
    RED.ChangeDutyCycle(b)


def transition(start_col, end_col, steps):
    old_r, old_g, old_b = start_col.get_centimal_vals()
    new_r, new_g, new_b = end_col.get_centimal_vals()

    rstep = new_r - old_r / steps
    gstep = new_g - old_g / steps
    bstep = new_b - old_b / steps
    set_rgb(start_col)

    for s in steps:
        curr_r = (255 * old_r + int(rstep*s))/100
        curr_g = (255 * old_g + int(gstep*s))/100
        curr_b = (255 * old_b + int(bstep*s))/100
        set_rgb(Color(curr_r, curr_g, curr_b))
        time.sleep(0.3)


while (True):
    morning_blue = Color(153, 204, 204)
    sand_yellow = Color(239, 221, 111)
    orange = Color(255, 153, 0)
    red = Color(255,0,0)
    white = Color(255, 255, 255)

    transition(morning_blue, sand_yellow, 50)
    transition(sand_yellow, orange, 50)
    transition(orange, red, 50)
    transition(red, white, 50)