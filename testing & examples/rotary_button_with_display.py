import time
from machine import Pin
import tm1637
from rotary_irq_rp2 import RotaryIRQ

rotary = RotaryIRQ(3, 2, range_mode=RotaryIRQ.RANGE_WRAP, pull_up=True)

btn = Pin(4, Pin.IN, Pin.PULL_UP) # button between gpio and ground

display = tm1637.TM1637(clk=Pin(5), dio=Pin(6))

# sets variable to be a certain number of digits
def zfl(s, width):
    # Pads the provided string with leading 0's to suit the specified 'chrs' length
    # Force # characters, fill with leading 0's
    return '{:0>{w}}'.format(s, w=width)

rot_val_old = rotary.value()  # Track the last known value of the encoder
rotary.set(value=2, min_val=-5, max_val=7)
while True:
    print(rotary.value())
    display.show("  " + str(zfl(rotary.value(),2)))

    
    if btn.value() == 0:  # Has the button been pressed?
        print("Reset encoder to:", 0)
        rotary.reset() # Resets the rotary library's internal counter back to zero
        
        time.sleep_ms(250) # A small delay to wait for the button to stop being pressed
        
"""        
    rot_val_new = rotary.value()  # What is the encoder value right now?
    
    if rot_val_old != rot_val_new:  # The encoder value has changed!
        print('Encoder value:', rot_val_new)
        
        rot_val_old = rot_val_new  # Track this change as the last know value
        display.show("  " + str(zfl(rot_val_new,2)))
 """