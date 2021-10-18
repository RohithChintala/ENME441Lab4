#!/usr/bin/python37all

# This code runs continually in the background to apply
# the stored PWM slider value to the GPIO output

import RPi.GPIO as GPIO
import time
import json

ledPin1 = 4
ledPin2 = 17
ledPin3 = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin1, GPIO.OUT)
GPIO.setup(ledPin2, GPIO.OUT)
GPIO.setup(ledPin3, GPIO.OUT)


pwm1 = GPIO.PWM(ledPin1, 1) # PWM object on our pin at 100 Hz
pwm1 = GPIO.PWM(ledPin2, 1) # PWM object on our pin at 100 Hz
pwm3 = GPIO.PWM(ledPin3, 1) # PWM object on our pin at 100 Hz
pwm1.start(50) 
pwm2.start(50) 
pwm3.start(50) 

while True:
 # with open("led_pwm.txt", 'r') as f:
  #  dutyCycle = float(f.read()) # read duty cycle value from file
 # pwm.ChangeDutyCycle(dutyCycle)
 # time.sleep(0.1)

  with open('lab4data.txt', 'r') as f:
    data = json.load(f)
    dutyCycle = float(data['slider1'])
  if data['L'] == 1:
    pwm1.ChangeDutyCycle(dutyCycle)
    time.sleep(0.1)
  if data['L'] == 2:
    pwm2.ChangeDutyCycle(dutyCycle)
    time.sleep(0.1)
  if data['L'] == 3:
    pwm3.ChangeDutyCycle(dutyCycle)
    time.sleep(0.1)



  #pwm.start(0) # start with LED off
  #print("slider 1 = "+ str(data['slider1']))
  #print("slider 2 = "+ str(data['slider2']))
  #dutyCycle = float(data['slider1'])
  #pwm.ChangeDutyCycle(dutyCycle)
  #time.sleep(0.1)