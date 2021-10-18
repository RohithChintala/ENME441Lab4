#!/usr/bin/python37all
import cgi
import json
data = cgi.FieldStorage()
s1 = data.getvalue('slider1')
l = float(data.getvalue('LED'))





if ('LED1' in data): # changed from OFF to ON
  L = 1
elif ('LED2' in data) : # changed from ON to OFF
  L = 2
elif ('LED3' in data) : # changed from ON to OFF
  L = 3
slide = {"slider1":s1, "l":l}
with open('led-pwm.txt', 'w') as f:
  json.dump(slide,f)





'''
with open('led-pwm.txt', 'w') as f:  
  f.write(str(s1))
'''
print('Content-type: text/html\n\n')
print('<html>')
print('<form action="/cgi-bin/led-pwm.py" method="POST">')
print('<input type="radio" name="LED1" value="LED1"> LED 1 <br>')
print('<input type="radio" name="LED2" value="LED2"> LED 2 <br>')
print('<input type="radio" name="LED3" value="LED3"> LED 3 <br>')
print('<input type="range" name="slider1" min="0" max="100" value="%s"><br>' % s1)
print('<input type="submit" value="Change LED brightness">')
print('</form>')
print('Brightness = %s' % s1)
print('</html>')