import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
OUTPIN = 15
GPIO.setup(OUTPIN, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
while True:
    for pin in range(30):
        try:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
            GPIO.output(pin, GPIO.HIGH) # Turn on
            print(pin)
            sleep(1) # Sleep for 1 second
            GPIO.output(pin, GPIO.LOW) # Turn off
            sleep(1) # Sleep for 1 second
        except:
            print("Cos nie tak z pinem: ")
            print(pin)

