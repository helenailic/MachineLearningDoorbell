import RPi.GPIO as GPIO

#import board
import neopixel
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
pixels = neopixel.NeoPixel (GPIO.output(18, True), 60)

pixels[0] = (255, 0, 0)


