# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Internal RGB LED red, green, blue example"""
import time
import board

if hasattr(board, "APA102_SCK"):
    import adafruit_dotstar

    led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
else:
    import neopixel

    led = neopixel.NeoPixel(board.NEOPIXEL, 1)

led.brightness = 0.1

while True:
    #summer colors
    led[0] = (35, 110, 150) #ocean blue
    time.sleep(1.3)
    led[0] = (255, 215, 0)  #sunny yellow
    time.sleep(1.3)
    led[0] = (255, 165, 0)  #orange
    time.sleep(1.3)
    led[0] = (255, 0, 0)    #bright red
    time.sleep(1.3)
    led[0] = (0, 0, 0)      #no light to indicate transition to next season
    time.sleep(3)

    #autumn colors
    led[0] = (96, 60, 20)  #chocolate brown
    time.sleep(1.3)
    led[0] = (212, 91, 18) #dark orange
    time.sleep(1.3)
    led[0] = (243, 188, 46) #yolk yellow
    time.sleep(1.3)
    led[0] = (95, 84, 38)   #dirty brown
    time.sleep(1.3)
    led[0] = (0, 0, 0)     #no light to indicate transition to next season
    time.sleep(3)

    #winter colors
    led[0] = (66, 104, 124)  #navy blue
    time.sleep(1.3)
    led[0] = (179, 218, 241) #baby blue
    time.sleep(1.3)
    led[0] = (112, 117, 113) #stone gray
    time.sleep(1.3)
    led[0] = (255, 255, 255) #snow white
    time.sleep(1.3)
    led[0] = (0, 0, 0)    #no light to indicate transition to next season
    time.sleep(3)

    #spring colors
    led[0] = (21, 178, 211) #sky blue
    time.sleep(1.3)
    led[0] = (255, 89, 143) #bright pink
    time.sleep(1.3)
    led[0] = (0, 241, 50)   #grass green
    time.sleep(1.3)
    led[0] = (100, 255, 100) #dull green
    time.sleep(1.3)
    led[0] = (0, 0, 0)  #no light to indicate transition to next season
    time.sleep(3)
