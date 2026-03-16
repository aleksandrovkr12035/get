import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)



led = 26
sensor = 6
GPIO.setup(led, GPIO.OUT)
GPIO.setup(sensor, GPIO.IN)

while True:
    state = GPIO.input(sensor)
    GPIO.output(led, not state)
    time.sleep(0.05)



