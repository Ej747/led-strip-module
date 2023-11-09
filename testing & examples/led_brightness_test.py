from machine import Pin
from utime import sleep
from neopixel import NeoPixel

strip_len = 300  # number of leds in strip. just remember, neopixel counts the first led as led[0]
strip_pin = Pin(0, Pin.OUT)  # gpio pin being used for led strip

strip = NeoPixel(strip_pin, strip_len)

bgt = r = g = b = 0


def clear():
    for i in range(strip_len): # don't need len - 1 because range func stops BEFORE specified number
        strip[i] = (0,0,0)
    strip.write()

# set all leds one color
def set_all():
    for i in range(strip_len): # don't need len - 1 because range func stops BEFORE specified number
        strip[i] = (int((bgt/100)*r), int((bgt/100)*g), int((bgt/100)*b))
    strip.write()

def set_some():
    if o == 0:
        set_all()

    if o != 0:
        clear()

    led_list=[0] # starts list for leds that will light up

    while led_list[-1] < (strip_len - o - 1): # if the last led number in the list is less than the length of the strip minus the offset minus 1
        led_list.append(led_list[-1] + o + 1) # add the offset plus 1 to the last number of the list

    for led_index in led_list: 
        strip[led_index] = (int((bgt/100)*r), int((bgt/100)*g), int((bgt/100)*b)) # set the leds to the strip

    strip.write() # write the leds to the strip


clear()
sleep(2)

r=100
g=0
b=0
o=3

bgt = 75
set_some()
sleep(1)

bgt = 50
set_some()
sleep(1)

bgt = 25
set_some()
sleep(1)


clear()