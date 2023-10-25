from utime import sleep
from machine import Pin

button = Pin(1, Pin.IN, Pin.PULL_DOWN)

menu_number = 1 #creates the menu variable and starts it at 1
print(menu_number)

while True:
    if button.value() == 1 and menu_number < 4:
        menu_number += 1
        print(menu_number)
        sleep(0.4)

    if button.value() == 1 and menu_number >= 4:
        menu_number = 1
        print(menu_number)
        sleep(0.4)