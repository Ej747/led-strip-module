from machine import Pin
from utime import sleep
import neopixel, tm1637
from rotary_irq_rp2 import RotaryIRQ

strip_len = 300  # number of leds in strip. just remember, neopixel counts the first led as led[0]
strip_pin = Pin(0)  # gpio pin being used for led strip

strip = neopixel.NeoPixel(strip_pin, strip_len) # sets neopixel to strip variable


rotary_p1 = 2 # left rotary pin
rotary_p2 = 3 # right rotary pin
rotary_button = Pin(4, Pin.IN, Pin.PULL_UP) # rotary button pin to gpio, other button pin to ground
rotary = RotaryIRQ(rotary_p2, rotary_p1, min_val=0, range_mode=RotaryIRQ.RANGE_WRAP, pull_up=True)

display = tm1637.TM1637(clk=Pin(5), dio=Pin(6)) # clk needs SCL and dio needs SDA


## setting vars
menu_number = 1
bgt = r = g = b = o = 0
bgt = 95     #just for testing. delete after
rot_val_old = 0
rot_val_new = 0


## defining functions
# clears all leds
def clear():
    for i in range(strip_len): # don't need len - 1 because range func stops BEFORE specified number
        strip[i] = (0,0,0)
    strip.write()

# set all leds one color
def set_all():
    for i in range(strip_len): # don't need len - 1 because range func stops BEFORE specified number
        strip[i] = (int((bgt/100)*r), int((bgt/100)*g), int((bgt/100)*b))
    strip.write()

# sets some leds with an evenly spaced offset (o)
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

# sets variable to be a certain number of digits
def zfl(s, width):
    # Pads the provided string with leading 0's to suit the specified 'chrs' length
    # Force # characters, fill with leading 0's
    return '{:0>{w}}'.format(s, w=width)

def rotarty_func(vrb_adj, max): # variable adjusted and max variable value
    rotary.set(value=vrb_adj, min_val=0, max_val=max) # not sure about syntax on this one, or if this is the right spot for it
    # I basically want to set the current encoder value to the current variable value so the variable doesn't jump to whatever the encoder was last
    # Also set the min and max values for the encoder (0-100 for brightness, 0-255 for rgb, and 0-half of the strip length for the offset)
    rot_val_old = vrb_adj # old value set to current value of the variable we're adjusting
    rot_val_new = rotary.value() # new value set to current rotary value

    if rot_val_old != rot_val_new: # if the old and new values are different
        vrb_adj = rotary.value() # make the variable we're adjusting set to the rotary value
        rot_val_old = rot_val_new # set the old value to the new value


## BEGINNING
clear() # clear the led strip
display.show("    ") # make the display blank
sleep(2)

while True:

    if rotary_button.value() == 0: # if rotary button is pushed
        menu_number += 1 # increase menu number by 1
        sleep(0.3) # delay to give time for letting go of button so it doesn't run again


    if menu_number == 1:
        display.show("8888") # just a placeholder for now. i'll make it blank for the final version
        # maybe add adjustment for brightness of display?
        print(menu_number, ": display should be off\nbright=", bgt, " r=", r, " b=", b, " g=", g, " o=", o) # just for computer terminal output
    
    if menu_number == 2:
        # let encoder adjust brightness variable
        rotarty_func(bgt, 100)
        # display brightness value
        display.show("L" + str(zfl(bgt,3)))
        print(menu_number, ": brightness value is: ", bgt)
        set_some()
    
    if menu_number == 3:
        # let encoder adjust r variable
        rotarty_func(r, 255)
        # display r value
        display.show("r" + str(zfl(r,3)))
        print(menu_number, ": r value is: ", r)
        set_some()

    if menu_number == 4:
        # let encoder adjust g variable
        rotarty_func(g, 255)
        # display g value
        display.show("g" + str(zfl(g,1)))
        print(menu_number, ": g value is: ", g)
        set_some()
    
    if menu_number == 5:
        # let encoder adjust b variable
        rotarty_func(b, 255)
        # display b value
        display.show("b" + str(zfl(b,3)))
        print(menu_number, ": b value is: ", b)
        set_some()

    if menu_number == 6:
        # let encoder adjust offset variable
        rotarty_func(o, o/2)
        # display offset value
        display.show("o" + str(zfl(o,3)))
        print(menu_number, ": offset value is: ", o)
        set_some()

    if menu_number > 6:
        menu_number = 1