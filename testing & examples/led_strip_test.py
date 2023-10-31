from machine import Pin
from utime import sleep
import neopixel

strip_len = 300  # number of leds in strip. just remember, neopixel counts the first led as led[0]
strip_pin = Pin(0)  # gpio pin being used for led strip

strip = neopixel.NeoPixel(strip_pin, strip_len)

brightness = r = g = b = 0


def clear():
    for i in range(strip_len): # don't need len - 1 because range func stops BEFORE specified number
        strip[i] = (0,0,0)
    strip.write()

# set all leds one color
def set_all():
    for i in range(strip_len): # don't need len - 1 because range func stops BEFORE specified number
        strip[i] = (int((brightness/100)*r), int((brightness/100)*g), int((brightness/100)*b))
    strip.write()


clear()
sleep(2)

brightness = 50
r=200
g=90
b=0

set_all()