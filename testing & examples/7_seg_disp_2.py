import tm1637
from machine import Pin
from utime import sleep

display = tm1637.TM1637(clk=Pin(5), dio=Pin(6))

menu_num = 2
color_num = 55

while True:
    display.number(menu_num)
    sleep(1)

    display.number(color_num)
    sleep(1)

    #display.numbers(menu_num:,color_num:)