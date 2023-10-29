from machine import Pin
from utime import sleep
import neopixel, tm1637
from rotary_irq_rp2 import RotaryIRQ

strip_len = 300  # number of leds in strip. just remember, neopixel counts the first led as led[0]
strip_pin = Pin(0)  # gpio pin being used for led strip

strip = neopixel.NeoPixel(strip_pin, strip_len) # sets neopixel to strip variable

rotary = RotaryIRQ(2, 3, min_val=0, range_mode=RotaryIRQ.RANGE_WRAP, pull_up=True) # sets rotary pins A and B to GPIO pins 2 and 3
rotary_button = Pin(4, Pin.IN, Pin.PULL_UP) # sets rotary button to GPIO pin 4

display = tm1637.TM1637(clk=Pin(5), dio=Pin(6))


# setting vars
menu_number = 1
brightness = r = g = b = o = 0
brightness = 7       #just for testing. delete after
rot_val_old = 0
rot_val_new = 0


# defining functions
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

# sets number (s) to be a certain number of digits
def zfl(s, width):
    # Pads the provided string with leading 0's to suit the specified 'chrs' length
    # Force # characters, fill with leading 0's
    return '{:0>{w}}'.format(s, w=width)

def rotarty_func(va, max): # variable adjusted and max variable value
    rotary.set(value=va, min_val=0, max_val=max, range_mode=RotaryIRQ.RANGE_WRAP)
    rot_val_old = va
    rot_val_new = rotary.value()

    if rot_val_old != rot_val_new:
        va = rotary.value()
        rot_val_old = rot_val_new


## BEGINNING
clear()
display.show("    ")
sleep(2)

while True:

    if rotary_button.value() == 0:
        menu_number += 1
        sleep(0.3)


    if menu_number == 1:
        display.show("8888")
        # add adjustment for 7 seg disp brightness?
        print(menu_number, ": display should be off\nbright=", brightness, " r=", r, " b=", b, " g=", g, " o=", o)
        #sleep(0.5)
    
    if menu_number == 2:
        # make encoder adjust brightness variable
        rotarty_func(brightness, 10)
        # display brightness value
        display.show("L" + str(zfl(brightness,3)))
        print(menu_number, ": brightness value is: ", brightness)
        #sleep(0.5)
    
    if menu_number == 3:
        # display r value
        display.show("r" + str(zfl(r,3)))
        # make encoder adjust r value
        print(menu_number, ": r value is: ", r)
        set_some(r,g,b,o)
        #sleep(0.5)

    if menu_number == 4:
        # display g value
        display.show("g" + str(zfl(g,1)))
        # make encoder adjust g value
        print(menu_number, ": g value is: ", g)
        set_some(r,g,b,o)
        #sleep(0.5)
    
    if menu_number == 5:
        # display b value
        display.show("b" + str(zfl(b,3)))
        # make encoder adjust b value
        print(menu_number, ": b value is: ", b)
        set_some(r,g,b,o)
        #sleep(0.5)

    if menu_number == 6:
        # display offset value
        display.show("o" + str(zfl(o,3)))
        # make encoder adjust offset value
        print(menu_number, ": offset value is: ", o)
        set_some(r,g,b,o)
        #sleep(0.5)

    if menu_number > 6:
        menu_number = 1