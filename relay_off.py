#!/usr/bin/python

# Import the required module.
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

# Set the mode of numbering the pins.
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)



GPIO.output( 11, True)
GPIO.output( 16, True)
GPIO.output( 18, True)
GPIO.output( 22, True)
