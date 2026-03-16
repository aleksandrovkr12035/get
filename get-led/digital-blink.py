import RPi.GPIO as GPIO
import time

led = 26
GPIO.setmode(GPIO.BCM)
botton = 13
GPIO.setup(led, GPIO.OUT)
GPIO.output(26, 1)

period = 1.0
GPIO.setup(botton, GPIO.IN)



state = 0

while True:
    state = not state
    GPIO.output(led, state)
    time.sleep(period)