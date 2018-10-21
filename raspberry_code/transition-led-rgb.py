import RPi.GPIO as GPIO
import time

# setup
RPIN = 23
GPIN = 24
BPIN = 25
FREQ = 100
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(RPIN, GPIO.OUT)
GPIO.setup(GPIN, GPIO.OUT)
GPIO.setup(BPIN, GPIO.OUT)
RED = GPIO.PWM(RPIN, FREQ)
RED.start(0)
GREEN = GPIO.PWM(GPIN, FREQ)
GREEN.start(0)
BLUE = GPIO.PWM(BPIN, FREQ)
BLUE.start(0)


class Color:
    def __init__(self, r, g, b, a=100):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def get_centimal_vals(self):
        return (self.a * self.r / 255,
                self.a * self.g / 255,
                self.a * self.b / 255
                )


def show_color(col):
    r, g, b = col.get_centimal_vals()
    show_rgb(r, g, b)


def show_rgb(r, g, b):
    RED.ChangeDutyCycle(r)
    GREEN.ChangeDutyCycle(g)
    RED.ChangeDutyCycle(b)


def transition(start_col, end_col, steps):
    old_r, old_g, old_b = start_col.get_centimal_vals()
    new_r, new_g, new_b = end_col.get_centimal_vals()

    rstep = (new_r - old_r) / steps
    gstep = (new_g - old_g) / steps
    bstep = (new_b - old_b) / steps

    show_color(start_col)

    for s in range(steps):
        curr_r = old_r + int(rstep*s)
        curr_g = old_g + int(gstep*s)
        curr_b = old_b + int(bstep*s)
        show_rgb(curr_r, curr_g, curr_b)
        time.sleep(0.3)


def sunrise_sequence():
    morning_blue = Color(153, 204, 204, 10)
    sand_yellow = Color(239, 221, 111, 20)
    orange = Color(255, 153, 0, 50)
    red = Color(255, 0, 0, 80)
    white = Color(255, 255, 255, 100)

    transition(morning_blue, sand_yellow, 50)
    transition(sand_yellow, orange, 50)
    transition(orange, red, 50)
    transition(red, white, 50)


if __name__ == '__main__':
    sunrise_sequence()