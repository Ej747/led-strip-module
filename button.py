from utime import sleep
from machine import Pin

button = Pin(1, Pin.IN, Pin.PULL_DOWN)

while True:
    print("Button value: ", button.value())
    sleep(0.25)