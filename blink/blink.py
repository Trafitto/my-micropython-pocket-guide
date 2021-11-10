from machine import Pin
import time
D4 = Pin(2, Pin.OUT)

while(True):
    D4.off() 
    time.sleep(2) 
    D4.on()
    time.sleep(2)                 