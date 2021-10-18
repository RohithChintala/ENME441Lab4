#!/usr/bin/python3

# This code runs continually in the background to apply
# the stored PWM slider value to the GPIO output

import RPi.GPIO as GPIO
import time
import json

ledPin1 = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin1, GPIO.OUT)

pwm = GPIO.PWM(ledPin, 100) # PWM object on our pin at 100 Hz
pwm.start(0) # start with LED off

while True:
 # with open("led_pwm.txt", 'r') as f:
  #  dutyCycle = float(f.read()) # read duty cycle value from file
  pwm.ChangeDutyCycle(dutyCycle)
  time.sleep(0.1)

  with open('led-pwm-multiple.txt', 'r') as f:
    data = json.load(f)
  #print("slider 1 = "+ str(data['slider1']))
  #print("slider 2 = "+ str(data['slider2']))
  dutyCycle = float(data['slider1'])
  pwm.ChangeDutyCycle(dutyCycle)
  time.sleep(0.1)