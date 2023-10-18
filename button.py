from utime import sleep
from machine import Pin

button = Pin(1, Pin.IN, Pin.PULL_DOWN)

menu_number = 1

while True:
    print(menu_number)
    sleep(0.2)

    if button.value() == 1 and menu_number < 4:
        menu_number += 1
        sleep(0.2)
    
    if button.value() == 1 and menu_number >= 4:
        menu_number = 1
        sleep(0.2)