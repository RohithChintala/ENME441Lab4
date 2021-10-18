#!/usr/bin/python37all

# put this file in /usr/lib/cgi-bin/led.py
# and associated html file in /var/www/html/led.html
# change owner and group if needed (probably not, but check that directories have correct permissions)
#       chown -R www-data /usr/lib/cgi-bin/led.py
#       chgrp -R www-data /usr/lib/cgi-bin/led.py

import RPi.GPIO as GPIO
import cgi
import json

# import and enable special exception handler for better error reporting
import cgitb
cgitb.enable()

ledPin1 = 19
ledPin2 = 20
ledPin3 = 21
L = 1

# GPIO setup:
GPIO.setmode(GPIO.BCM)      # choose pin numbering convention (alt = BOARD)
GPIO.setwarnings(False)     # ignore warnings due to multiple scripts at same time
GPIO.setup(ledPin1, GPIO.OUT)
GPIO.setup(ledPin2, GPIO.OUT)
GPIO.setup(ledPin3, GPIO.OUT)


# Begin generatation of web page showing current state:
print('Content-type:text/html\n\n')    # blank line = end of headers
print('<html>')
print('<head>')
print('<title>LED switch test</title>')
print('<meta http-equiv="refresh" content="5">')  # refresh to update LED state
print('</head>')
print('<body>')
print('<div style="width:600px;background:#AAAAFF;border:1px;text-align:center">')
print('<br>')
print('<font size="3" color="black" face="helvetica">')
print('<b>LED switch</b>')
print('<br><br>')

# look at POST data for either 'on' or 'off' button names, using 
# "if ('on' in form)" instead of data.getvalue() since we have 2 different
# button names (unlike prior example with a single button name & 2 button values): 
form = cgi.FieldStorage() # get POST data

'''
if ('on' in form): # changed from OFF to ON
  GPIO.output(ledPin, 1)
elif ('off' in form) : # changed from ON to OFF
  GPIO.output(ledPin, 0)
'''

if ('LED1' in form): # changed from OFF to ON
  GPIO.output(ledPin1, 1)
  L = 1
elif ('LED2' in form) : # changed from ON to OFF
  GPIO.output(ledPin2, 1)
  L = 2
elif ('LED3' in form) : # changed from ON to OFF
  GPIO.output(ledPin3, 1)
  L = 3

data = cgi.FieldStorage()
#p = data.getvalue('slider1')
s1 = data.getvalue('slider1')

#s2 = data.getvalue('slider2')
data = {"slider1":s1, "L":L}
with open('lab4data.txt', 'w') as f:
  json.dump(data,f)


#with open('lab4.txt', 'w') as f: 
 # f.write(str(p))


# display current LED state to user:
if GPIO.input(ledPin1):
  print('hello')
else:
  print('<font color="black"> LED IS OFF')
print('<font color="black">')
print('<br><br>')


# Create the buttons to change LED state.  Use 'target="_blank"
# to open in a new window if desired:
#print('<form action="/cgi-bin/led.py" method="POST" target="_self">')
#print('<input type="submit" name="on" value="Turn LED ON" />')
#print('<input type="submit" name="off" value="Turn LED OFF" />')
#print('</form>')

print('<form action="/cgi-bin/lab4.py" method="POST" target="_self">')
print('<input type="radio" name="led" value="LED1" checked> LED 1 <br>')
print('<input type="radio" name="led" value="LED2"> LED 2 <br>')
print('<input type="radio" name="led" value="LED3"> LED 3 <br>')
print('<input type="submit" value="Submit">')
print('<input type="range" name="slider1" min ="0" max="100" value ="50"/><br>')
print('</form>')


print('<br>')
print('</body>')
print('</html>')


