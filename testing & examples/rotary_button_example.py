"""
A simple example showing how to handle a button press from a rotary encoder

Requires the RotaryIRQ library from https://github.com/miketeachman/micropython-rotary
"""

import time
from machine import Pin
from rotary_irq_rp2 import RotaryIRQ

# Enter the two GPIO pins you connected to data pins A and B
# Note the order of the pins isn't strict, swapping the pins
# will swap the direction of change.
rotary = RotaryIRQ(3, 2, range_mode=RotaryIRQ.RANGE_WRAP, pull_up=True)

# If you're using a Standalone Rotary Encoder instead of a module,
# you might need to enable the internal pull-ups on the Pico
# rotary = RotaryIRQ(2, 3, pull_up=True)

# Enter the pin that SW is connected to on the Pico
btn = Pin(4, Pin.IN, Pin.PULL_UP) # button between gpio and ground

# Note: the encoder we're using has a built in pull-up on the push button
#  if you're using a plain rotary encoder you might want to enable the
#  built in pull-up on the Pico with:

# btn = Pin(12, Pin.IN, Pin.PULL_UP)

rot_val_old = rotary.value()  # Track the last known value of the encoder
rotary.set(value=2, min_val=-5, max_val=7)
while True:
    
    if btn.value() == 0:  # Has the button been pressed?
        print("Reset encoder to:", 0)
        rotary.reset() # Resets the rotary library's internal counter back to zero
        
        time.sleep_ms(250) # A small delay to wait for the button to stop being pressed
        
        
    rot_val_new = rotary.value()  # What is the encoder value right now?
    
    if rot_val_old != rot_val_new:  # The encoder value has changed!
        print('Encoder value:', rot_val_new)
        
        rot_val_old = rot_val_new  # Track this change as the last know value

