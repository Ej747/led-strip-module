from machine import Pin, ADC
from utime import sleep
import neopixel, tm1637

strip_len = 300  # number of leds in strip. just remember, neopixel counts the first led as led[0]
strip_pin = Pin(0)  # gpio pin being used for led strip

strip = neopixel.NeoPixel(strip_pin, strip_len)

# button gpio pin. will probably change later bc of encoder
button = Pin(1, Pin.IN, Pin.PULL_DOWN)

pot = ADC(26)
# pot vals: low=500, high 65535


# defining functions
# map function
def map(x, in_min, in_max, out_min, out_max):
    # maps 2 ranges together
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

# clears all leds
def clear():
    for i in range(strip_len): # don't need len - 1 because range func stops BEFORE specified number
        strip[i] = (0,0,0)
    strip.write()

# set all one color
def set_all(r, g, b):
    for i in range(strip_len): # don't need len - 1 because range func stops BEFORE specified number
        strip[i] = (r, g, b)
    strip.write()

# set leds with evenly spaced offset (o)
def set_some(r, g, b, o):
    if o == 0:
        set_all(r, g, b)

    if o != 0:
        clear()

    led_list=[0] # starts list for leds that will light up

    while led_list[-1] < (strip_len - o - 1):
        led_list.append(led_list[-1] + o + 1)

    for led_index in led_list:
        strip[led_index] = (r, g, b)

    strip.write()


# setting vars
menu_number = 1
brightness = 0
r = 0
g = 0
b = 0
o = 0


## BEGINNING
clear()
sleep(2)

while True:
    # 'makes' 6 menus (off, brightness, r, g, b, offset)
    if button.value() == 1 and menu_number < 6:
        menu_number += 1
        sleep(0.2)

    if button.value() == 1 and menu_number >= 6:
        menu_number = 1
        sleep(0.2)

    pot_value = pot.read_u16()
    color_value = map(pot_value, 500, 65535, 0, 255)
    bright_value = map(pot_value, 500, 65535, 0, 100)
    offset_value = map(pot_value, 500, 65535, 0, 10)

    if menu_number == 1:
        # display 0 then turn off 7 seg disp
        print(menu_number, ": display should be off\nbright=", brightness, " r=", r, " b=", b, " g=", g, " o=", o)
        #sleep(0.5)
    
    if menu_number == 2:
        # display brightness value
        # make encoder adjust brightness variable
        print(menu_number, ": brightness value is: ", bright_value)
        brightness = bright_value
        #sleep(0.5)
    
    if menu_number == 3:
        # display r value
        # make encoder adjust r value
        print(menu_number, ": r value is: ", r)
        r = color_value
        set_some(r,g,b,o)
        #sleep(0.5)

    if menu_number == 4:
        # display g value
        # make encoder adjust g value
        print(menu_number, ": g value is: ", g)
        g = color_value
        set_some(r,g,b,o)
        #sleep(0.5)
    
    if menu_number == 5:
        # display b value
        # make encoder adjust b value
        print(menu_number, ": b value is: ", b)
        b = color_value
        set_some(r,g,b,o)
        #sleep(0.5)

    if menu_number == 6:
        # display offset value
        # make encoder adjust offset value
        print(menu_number, ": offset value is: ", o)
        o = offset_value
        set_some(r,g,b,o)
        #sleep(0.5)
