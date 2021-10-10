
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering

GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW)   # Set pin 11 to be an output pin and set initial value to low (off)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)   # Set pin 13 to be an output pin and set initial value to low (off)
GPIO.setup(15, GPIO.OUT, initial=GPIO.LOW)   # Set pin 15 to be an output pin and set initial value to low (off)

sleep(1)

GPIO.output(11, GPIO.HIGH)

sleep(1)

GPIO.output(13, GPIO.HIGH)

sleep(1)

GPIO.output(15, GPIO.HIGH)

sleep(1)

GPIO.output(11, GPIO.LOW)

sleep(1)

GPIO.output(13, GPIO.LOW)

sleep(1)

GPIO.output(15, GPIO.LOW)