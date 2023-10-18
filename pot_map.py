from machine import ADC, Pin, PWM

pot = ADC(26)
led = PWM(Pin(7))
led.freq(1000)

# pot vals: low=500, high 65535

def map(x, in_min, in_max, out_min, out_max):
    # maps 2 ranges together
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)


while True:
    #print("Value is: ", pot.read_u16())
    #led.duty_u16(pot.read_u16())

    pot_value = pot.read_u16()
    percentage = map(pot_value, 500, 65535, 0, 100)

    led_value = map(percentage, 0, 100, 0, 65535)
    print("Percentage: ", percentage, " Raw: ", pot_value, " Led value: ", led_value)
    led.duty_u16(led_value) 