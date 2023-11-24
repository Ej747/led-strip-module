import machine
import neopixel
import time
import tm1637
from rotary_irq_rp2 import RotaryIRQ

# 4 digit 7 segment display setup
tm = tm1637.TM1637(clk=machine.Pin(5), dio=machine.Pin(6))

# Pins for the rotary encoder
# not sure about the naming for clk and dt. the rotary just has the pins, they're not really labeled. the 7 seg disp has clk and dio
clk_pin = machine.Pin(2)  # GPIO pin number
dt_pin = machine.Pin(3)   # GPIO pin number
sw_pin = machine.Pin(4)   # GPIO pin number     # presumably the rotary button pin? (sw means switch?)

# Rotary object
r = RotaryIRQ(dt_pin, clk_pin, pull_up=True)
# what i did with the other code is i set up the rotary with the rotary pins but treated the button pin as a completely seperate button
# like this:
r_button = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)

# LED settings
num_leds = 300  # Number of LEDs in the strip
led_pin = machine.Pin(0)  # GPIO pin number for the LED strip
strip = neopixel.NeoPixel(led_pin, num_leds)

# LED color and brightness settings
led_colors = [(255, 0, 0)] * num_leds  # Initial color (red) for all LEDs
brightness = 0.3  # Initial brightness

# Define the last digit of the 4-Digit display
color_digit = 0  # 0 indicates no color selection

def set_color(color):
    for i in range(num_leds):
        strip[i] = color[i]
    strip.write()

while True:
    delta = r.value()

    if r_button.value() == 0: # if rotary button is pushed
        color_digit += 1 # increase color digit by 1
        time.sleep(0.3) # delay to give time for letting go of button so it doesn't run again
    
    # Change the LED color based on rotary encoder input
    if delta != 0:
        if delta > 0:
            # Increase the color component for the selected LED
            led_colors[color_digit - 1] = (
                min(255, led_colors[color_digit - 1][0] + 10),
                min(255, led_colors[color_digit - 1][1] + 10),
                min(255, led_colors[color_digit - 1][2] + 10),
            )
        else:
            # Decrease the color component for the selected LED
            led_colors[color_digit - 1] = (
                max(0, led_colors[color_digit - 1][0] - 10),
                max(0, led_colors[color_digit - 1][1] - 10),
                max(0, led_colors[color_digit - 1][2] - 10),
            )
        
        set_color(led_colors)
    
    current_color = ?

    # Update the color_digit based on the selected color
    if current_color == (255, 0, 0):  # Red
        color_digit = 1
    elif current_color == (0, 255, 0):  # Green
        color_digit = 2
    elif current_color == (0, 0, 255):  # Blue
        color_digit = 3
    
    # Display the color_digit on the 4-Digit LED Segment Display Module
    display_color = [current_color[0] // 10, current_color[1] // 10, current_color[2] // 10, color_digit]
    tm.number(display_color)
    
    time.sleep(0.1)  # Optional delay to prevent excessive updates
