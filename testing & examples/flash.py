from machine import Pin
from utime import sleep

# onboard led
pin = Pin("LED", Pin.OUT)

print("LED starts flashing...")
while True:
    pin.on()
    sleep(0.5)
    pin.off()
    sleep(0.5)