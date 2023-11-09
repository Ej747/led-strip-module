# This file can basically be ignored. I was using it for testing when I was using a potentiometer instead of a rotary encoder

from machine import ADC #analog-digital conversion
from utime import sleep #for sleep command

pot = ADC(26) #sets potemtiometer to GPIO pin 26 (not board pin 26)

while True:
    print("Value is", pot.read_u16())
    sleep(0.25)