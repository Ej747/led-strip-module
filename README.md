# led-strip-module
Not exactly necessary to make a github page for this as it's a single python file, but I figured it would be easier to keep track of changes.
Powered by a Raspbery Pi Pico running micropython, this controls a strip of ws2812b eco leds.

Going to design a case in onshape to be 3d printed. Not sure of material yet.

Hardware:

HiLetgo tm1637 4 digit 7 segment display: https://www.amazon.com/gp/product/B01DKISMXK/ref=ox_sc_act_title_1?smid=A30QSGOJR8LMXA&psc=1

Taiss KY-040 rotary encoder: https://www.amazon.com/gp/product/B07F26CT6B/ref=ox_sc_act_title_5?smid=A2VILSBUHD1UD8&psc=1
	Planning on using this unless the 20 pulse/rotation is too small. It might be a pain to have to rotate so much (think 0-255 for rgb vals).
 	Alternate is an Adafruit 100 pulse/rotation encoder: https://www.adafruit.com/product/5734
	If I end up using the Adafruit one, I'll buy a button for the 'menu' control: https://www.amazon.com/gp/product/B07RTZVZ6L/ref=ox_sc_saved_title_2?smid=AGOSLUO29ZUJ2&psc=1
