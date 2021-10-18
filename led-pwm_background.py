#!/usr/bin/python3

# This code runs continually in the background to apply
# the stored PWM slider value to the GPIO output

import RPi.GPIO as GPIO
import time
import json

ledPin1 = 19
ledPin2 = 17
ledPin3 = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)


pwm1 = GPIO.PWM(ledPin1, 100) # PWM object on our pin at 100 Hz
pwm1.start(0) # start with LED off
pwm2 = GPIO.PWM(ledPin2, 100) # PWM object on our pin at 100 Hz
pwm2.start(0) # start with LED off
pwm3 = GPIO.PWM(ledPin3, 100) # PWM object on our pin at 100 Hz
pwm3.start(0) # start with LED off

while True:
  with open('led-pwm.txt', 'r') as f:
    data = json.load(f)
    dutyCycle = float(data['slider1'])
 
if data['L'] == 'LED1':
  pwm1.ChangeDutyCycle(dutyCycle)
  time.sleep(0.1)
if data['L'] == 'LED2':
  pwm2.ChangeDutyCycle(dutyCycle)
  time.sleep(0.1)
if data['L'] == 'LED3':
  pwm3.ChangeDutyCycle(dutyCycle)
  time.sleep(0.1)

#pwm1.ChangeDutyCycle(dutyCycle)
#time.sleep(0.1)
'''
while True:
  with open("led-pwm.txt", 'r') as f:
    dutyCycle = float(f.read()) # read duty cycle value from file
  pwm1.ChangeDutyCycle(dutyCycle)
  time.sleep(0.1)
'''