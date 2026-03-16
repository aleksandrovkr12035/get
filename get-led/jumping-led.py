import RPi.GPIO as GPIO
import time

leds = [24, 22, 23, 27, 17, 25, 12, 16]
GPIO.setmode(GPIO.BCM)
botton = 13
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)
GPIO.setup(botton, GPIO.IN)

light_time = 0.2

for led in leds:
    GPIO.output(led, 1)
    time.sleep(light_time)
    GPIO.output(led, 0)

for led in reversed(leds):
    GPIO.output(led, 1)
    time.sleep(light_time)
    GPIO.output(led, 0)