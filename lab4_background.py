#!/usr/bin/python3

# This code runs continually in the background to apply
# the stored PWM slider value to the GPIO output

import RPi.GPIO as GPIO
import time
import json

ledPin1 = 19
ledPin2 = 20
ledPin3 = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin1, GPIO.OUT)
GPIO.setup(ledPin2, GPIO.OUT)
GPIO.setup(ledPin3, GPIO.OUT)


pwm1 = GPIO.PWM(ledPin1, 100) # PWM object on our pin at 100 Hz
pwm1 = GPIO.PWM(ledPin2, 100) # PWM object on our pin at 100 Hz
pwm3 = GPIO.PWM(ledPin3, 100) # PWM object on our pin at 100 Hz
pwm1.start(0) 
pwm2.start(0) 
pwm3.start(0) 

while True:
 # with open("led_pwm.txt", 'r') as f:
  #  dutyCycle = float(f.read()) # read duty cycle value from file
 # pwm.ChangeDutyCycle(dutyCycle)
 # time.sleep(0.1)

  with open('led-pwm-multiple.txt', 'r') as f:
    data = json.load(f)
  dutyCycle = float(data['slider1'])
  if data['L'] == 1:
    pwm1.ChangeDutyCycle(dutyCycle)
  if data['L'] == 2:
    pwm2.ChangeDutyCycle(dutyCycle)
  if data['L'] == 3:
    pwm3.ChangeDutyCycle(dutyCycle)



  #pwm.start(0) # start with LED off
  #print("slider 1 = "+ str(data['slider1']))
  #print("slider 2 = "+ str(data['slider2']))
  #dutyCycle = float(data['slider1'])
  #pwm.ChangeDutyCycle(dutyCycle)
  #time.sleep(0.1)