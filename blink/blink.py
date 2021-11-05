from machine import Pin
import time
D2 = Pin(2, Pin.OUT)

while(True):
    D2.off() 
    time.sleep(2) 
    D2.on()
    time.sleep(2)                 