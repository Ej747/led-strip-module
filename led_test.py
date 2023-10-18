from machine import Pin
from utime import sleep
import neopixel


strip_len = 300  # number of leds in strip
strip_pin = Pin(0)  # gpio pin being used for led strip

strip = neopixel.NeoPixel(strip_pin, strip_len)

# clears all leds
def clear():
    for i in range(strip_len):
        strip[i] = (0,0,0)
    strip.write()

# set all one color
def set_all(r, g, b):
    for i in range(strip_len):
        strip[i] = (r, g, b)
    strip.write()



while True:
    clear()
    sleep (2)
    #just an example of how to control individual ones
    strip[0] = (255,0,0)
    strip[2] = (255,255,0)
    strip[4] = (0,255,0)
    strip[6] = (0,255,255)
    strip[8] = (0,0,255)
    strip[10] = (255,255,255)

    # DONT' FORGET THIS
    strip.write()

    # off after 10 sec
    sleep(3)
    clear()
    sleep(2)

    for i in range(0, 150, 1):
        set_all(i, 0, 0)
        sleep(0.001)

    sleep(1)

    for i in range(150, 0, -1):
        set_all(i, 0, 0)
        sleep(0.001)

    sleep(1)