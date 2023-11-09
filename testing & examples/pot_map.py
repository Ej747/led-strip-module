# This file can basically be ignored. I was using it for testing when I was using a potentiometer instead of a rotary encoder

from machine import ADC, Pin, PWM

pot = ADC(26)
led = PWM(Pin(7))
led.freq(1000)

pot_low=500
pot_high=65535

def map(x, in_min, in_max, out_min, out_max):
    # maps 2 ranges together
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)


while True:
    #print("Value is: ", pot.read_u16())
    #led.duty_u16(pot.read_u16())

    pot_value = pot.read_u16()
    percentage = map(pot_value, pot_low, pot_high, 0, 100)

    led_value = map(percentage, 0, 100, 0, 65535)
    print("Percentage: ", percentage, " Raw: ", pot_value, " Led value: ", led_value)
    led.duty_u16(led_value)