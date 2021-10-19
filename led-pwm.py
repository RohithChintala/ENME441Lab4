#!/usr/bin/python37all
import cgi
import json
data = cgi.FieldStorage()
s1 = data.getvalue('slider1')
L = data.getvalue('LED')


print('Content-type:text/html\n\n')    # blank line = end of headers
print('<html>')
print('<head>')
print('<title>LED switch test</title>')
print('<meta http-equiv="refresh" content="60">') 
print('</head>')
print('<body>')
print('<div style="width:600px;background:#AAAAFF;border:1px;text-align:center">')
print('<br>')
print('<font size="3" color="black" face="helvetica">')
print('<b>Lab 4 LED PWM </b>')
print('<br><br>')


slide = {"slider1":s1, "Le":L}
with open('led-pwm.txt', 'w') as f:
  json.dump(slide,f)





'''
with open('led-pwm.txt', 'w') as f:  
  f.write(str(s1))
'''
#print('Content-type: text/html\n\n')
print('<html>')
print('<form action="/cgi-bin/led-pwm.py" method="POST">')
print('<input type="radio" name="LED" value="a"> LED 1 <br>')
print('<input type="radio" name="LED" value="b"> LED 2 <br>')
print('<input type="radio" name="LED" value="c"> LED 3 <br>')
print('<input type="range" name="slider1" min="0" max="100" value="%s"><br>' % s1)
print('<input type="submit" value="Change LED brightness">')
print('</form>')
print('Brightness = %s' % s1)
print('LED =', L)
print('</html>')

#<input type="submit" value="Change LED brightness">