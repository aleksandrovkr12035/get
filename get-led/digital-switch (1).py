import RPi.GPIO as GPIO
import time


led = 26
GPIO.setmode(GPIO.BCM)
botton = 13
GPIO.setup(26, GPIO.OUT)
GPIO.output(26, 1)
GPIO.setup(botton, GPIO.IN)

state = 0

while True:
    if GPIO.input(botton):
        state = not state
        GPIO.output(led, state)
        time.sleep(0.2)
