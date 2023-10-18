from machine import PWM, Pin, ADC
from utime import sleep

pot = ADC(26)

while True:
    print("Value is", pot.read_u16())