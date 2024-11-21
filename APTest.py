"""
Turns on a Wi-Fi AP for the ESP32

You can connect to this AP from a computer or mobile phone

Network Name: ESP_AP
Passcode: 123456789
You can change the passcode and network name by changing the password and ssid variables

When you run this code, it will persistenly enable the AP, meaning that it will still be 
there even if you reboot. IT IS RECOMMENDED TO RUN 'APTerminator.py' ONCE YOU'RE DONE WITH
THE AP TO ENSURE THAT YOU DON'T GET HACKED!!

Once connected, navigate to the IP address printed in the console to get a web page
"""
try:
 import usocket as socket        #importing socket
except:
 import socket
import network            #importing network
import esp                 #importing ESP
from machine import Pin
esp.osdebug(None)
import gc
gc.collect()
ssid = 'ESP_AP'                  # Set access point name 
password = '123456789'      # Set your access point password


ap = network.WLAN(network.AP_IF)
ap.active(True)            #activating
ap.config(ssid=ssid, hidden = False, key=password, security = 3) # security: 2: WPA, 3: WPA2

while ap.active() == False:
  pass

print('Connection is successful')
print(ap.ifconfig())

def web_page(): # Customize to your liking
  html = "thing"
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #creating socket object
s.bind(('', 80))
s.listen(5)

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  print('Content = %s' % str(request))
  Pin(2, Pin.OUT).value(1)
  response = web_page()
  conn.send(response)
  conn.close()