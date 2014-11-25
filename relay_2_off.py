#!/usr/bin/python

# Import the required module.
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

# Set the mode of numbering the pins.
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT) #1
GPIO.setup(16, GPIO.OUT) #2
GPIO.setup(18, GPIO.OUT) #3
GPIO.setup(22, GPIO.OUT) #4


GPIO.output( 16, True) # 2
