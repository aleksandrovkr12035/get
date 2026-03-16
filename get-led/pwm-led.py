import RPi.GPIO as GPIO
import time


led = 26
GPIO.setmode(GPIO.BCM)
botton = 13
GPIO.setup(26, GPIO.OUT)
GPIO.output(26, 1)

pwm = GPIO.PWM(led, 200)
duty = 0.0
pwm.start(duty)

GPIO.setup(botton, GPIO.IN)

while True:
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.05)

    duty += 1.0
    if duty > 100.0:
        duty = 0.0