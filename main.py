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
loop_check = [0, 0, 0, 0, 0, 0]


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

    if o != 0 and loop_check[menu_number - 1] == 0:
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
    if loop_check[menu_number - 1] == 0:
        rotary.set(value=vrb_adj, min_val=0, max_val=max)
        loop_check[menu_number - 1] = 1

    #vrb_adj = rotary.value()

## BEGINNING
clear() # clear the led strip
display.show("8888")
sleep(1)
display.show("    ")

while True:

    if rotary_button.value() == 0: # if rotary button is pushed
        menu_number += 1 # increase menu number by 1
        sleep(0.3) # delay to give time for letting go of button so it doesn't run again


    if menu_number == 1:
        display.show("8888") # just a placeholder for now. i'll make it blank for the final version
        # maybe add adjustment for brightness of display?
        if loop_check[menu_number-1] == 0:
            print(menu_number, ": display should be off\nbright=", bgt, " r=", r, " b=", b, " g=", g, " o=", o) # just for computer terminal output
            loop_check[menu_number - 1] = 1
        
    if menu_number == 2:
        # let encoder adjust brightness variable
        print(menu_number, ": bgt: ", bgt, ", loop-check: ", loop_check[menu_number - 1], rotary.value())
        rotarty_func(bgt, 100)
        bgt = rotary.value()
        # display brightness value
        display.show("L" + str(zfl(bgt,3)))
        set_some()
    
    if menu_number == 3:
        # let encoder adjust r variable
        print(menu_number, ": r: ", r, ", loop-check: ", loop_check[menu_number - 1], rotary.value())
        rotarty_func(r, 255)
        r = rotary.value()
        # display r value
        display.show("r" + str(zfl(r,3)))
        set_some()

    if menu_number == 4:
        # let encoder adjust g variable
        print(menu_number, ": g: ", g, ", loop-check: ", loop_check[menu_number - 1], rotary.value())
        rotarty_func(g, 255)
        g = rotary.value()
        # display g value
        display.show("g" + str(zfl(g,3)))
        set_some()
    
    if menu_number == 5:
        # let encoder adjust b variable
        print(menu_number, ": b: ", b, ", loop-check: ", loop_check[menu_number - 1], rotary.value())
        rotarty_func(b, 255)
        b = rotary.value()
        # display b value
        display.show("b" + str(zfl(b,3)))
        set_some()

    if menu_number == 6:
        # let encoder adjust offset variable
        print(menu_number, ": offset: ", o, ", loop-check: ", loop_check[menu_number - 1], rotary.value())
        rotarty_func(o, int(strip_len/2))
        o = rotary.value()
        # display offset value
        display.show("o" + str(zfl(o,3)))
        set_some()

    if menu_number > 6:
        for i in range(len(loop_check)):
            loop_check[i-1] = 0
        menu_number = 1