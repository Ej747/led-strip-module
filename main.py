import machine
import rotary
import neopixel
import time

# Pins for the rotary encoder
clk_pin = machine.Pin(0)  # GPIO pin number
dt_pin = machine.Pin(1)   # GPIO pin number
sw_pin = machine.Pin(2)   # GPIO pin number

# Rotary object
r = rotary.Rotary(clk_pin, dt_pin, sw_pin)

# LED settings
num_leds = 300  # Number of LEDs in the strip
led_pin = machine.Pin(3)  # GPIO pin number for the LED strip
strip = neopixel.NeoPixel(led_pin, num_leds)

# LED color and brightness settings
led_colors = [(255, 0, 0)] * num_leds  # Initial color (red) for all LEDs
brightness = 0.5  # Initial brightness

# Define the last digit of the 4-Digit display
color_digit = 0  # 0 indicates no color selection

def set_color(color):
    for i in range(num_leds):
        strip[i] = color[i]
    strip.write()

while True:
    delta = r.read()
    
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
