import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
OUTPIN = 8
GPIO.setup(OUTPIN, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
while True:
    GPIO.output(OUTPIN, GPIO.HIGH) # Turn on
    sleep(1) # Sleep for 1 second
    GPIO.output(OUTPIN, GPIO.LOW) # Turn off
    sleep(1) # Sleep for 1 second

