#!/usr/bin/python37all

import cgi
import json
data = cgi.FieldStorage()
s1 = data.getvalue('slider1') #gets slider value from website
L = data.getvalue('LED') #gets led value from website

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
#print('<title>LED switch test</title>')
#print('<meta http-equiv="refresh" content="60">') 
print('</head>')
print('<body>')
print('<div style="width:600px;background:#40E0D0;border:1px;text-align:center">')
print('<br>')
print('<font size="3" color="black" face="helvetica">')
print('<b>Lab 4 LED PWM </b>')
print('<br><br>')

slide = {"slider1":s1, "Le":L} #creates slide dictionary for slider and Led variables
with open('led-pwm.txt', 'w') as f: #opens led-pwm.txt file
  json.dump(slide,f) #uses json to dump dictionary into file

print('<html>')
print('<form action="/cgi-bin/led-pwm.py" method="POST">')
print('<input type="radio" name="LED" value="1"> LED 1 <br>')
print('<input type="radio" name="LED" value="2"> LED 2 <br>')
print('<input type="radio" name="LED" value="3"> LED 3 <br>')
print('<input type="range" name="slider1" min="0" max="100" value="%s"><br>' % s1)
print('<input type="submit" value="Change Chosen LED Brightness">')
print('</form>')
print('Brightness = %s' % s1)
print('LED =', L)
print('</html>')
