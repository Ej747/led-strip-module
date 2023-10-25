import tm1637
from machine import Pin
from utime import sleep

display = tm1637.TM1637(clk=Pin(5), dio=Pin(6))
num_variable = 255
short_string = "WORD"
long_string = "STRINGS ARE FUN"

while True:
    # Show a word
    display.show("COOL")
    sleep(1)

    display.show("23"+"EJ")
    sleep(1)

    display.number(num_variable)
    sleep(1)

    display.show(short_string)
    sleep(1)

    display.scroll(long_string)
    sleep(1)
     
    #blank the screen
    display.show("    ")
    sleep(1)
     
    #show numbers
    display.number(-502)
    sleep(4)

    display.show("    ")
    sleep(1)

    display.number(-418)
    sleep(4)

    #show scrolling text
    display.scroll("PICO IS COOL")
    sleep(1)
     
     
    #show temperature
    display.temperature(34)
    sleep(1)
     

    # Show a word
    display.show("COOL")
    sleep(1)
     
    #adjust the brightness to make it loewr
    for x in range(8):
        display.brightness(x)
        print(x)
        sleep(1)
 