import RPi.GPIO as GPIO
import time

def dec2bin(value):
    return [int(element) for element in bin(value)[2::].zfill(8)]

GPIO.setmode(GPIO.BCM)

leds = [16, 12, 25, 17, 27, 23, 22, 24]
up = 9
down = 10

GPIO.setup(leds, GPIO.OUT)
GPIO.setup(up, GPIO.IN)
GPIO.setup(down, GPIO.IN)
GPIO.output(leds, 0)

num = 0

sleep_time = 0.2

while True:
    if GPIO.input(up):
        num = min((num+1), 255)
        time.sleep(sleep_time)
        print(num, dec2bin(num))

    if GPIO.input(down):
        num = num + 1
        time.sleep(sleep_time)
        print(num, dec2bin(num))

    

    GPIO.output(leds, dec2bin(num))