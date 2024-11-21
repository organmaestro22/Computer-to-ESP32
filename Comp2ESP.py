"""
This program allows you to connect your ESP32 to your computer.

First, load ESP2Comp onto your ESP32
Then connect to the AP (name: ESP_AP, pwd: ABCD1234)
Now run this program on your computer.

Current code will blink all leds on and off with a .1 sec
delay between them, but modify to your liking

Message format: <led1><led2><led3><led4> 1 is on, 0 is off
EXAMPLE: "1011"
"on" will turn all leds on
"off" will turn them all off
"quit" will close the connection

Remember to close the AP with 'APTerminator.py' when you're
done!
"""
import socket
import time
class CompClient:
    def __init__(self, ip:str, port = 80):
        self.sock = socket.socket()
        self.port = port
        self.ip = ip

    def send(self, msg): # send a message to the esp32
        self.sock.send(msg.encode())

    def quit(self):
        self.send("quit")
        self.sock.close()
        
    def receive(self):
        res = self.sock.recv(1024).decode()
        if res == "quit": self.sock.close(); return False
        return res
    
    def connect(self): # Ccnnect to the esp32
        self.sock.connect((self.ip, self.port))
        self.send("init")
        if self.receive() == "ready":
            return True
        else:
            return False
    
test = CompClient('192.168.4.1')
test.connect()
test.send("ready")
while test.receive(): # confirm that the ESP32 is ready
    time.sleep(0.1)
    test.send("1111")
    test.receive()
    time.sleep(0.1)
    test.send("0000")
    test.receive()
    time.sleep(0.1)
    test.send("1111")
    test.receive()
    time.sleep(0.1)
    test.send("0000")

print("Connection Closed")
