import RPi.GPIO as GPIO
import time

class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose=False):
        self.gpio_pin = gpio_pin
        self.dynamic_range = dynamic_range
        self.pwm_frequency = pwm_frequency
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)  
        GPIO.setup(self.gpio_pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.gpio_pin, self.pwm_frequency)  
        self.pwm.start(0)  
    
    def deinit(self):
        self.pwm.stop()  
        GPIO.output(self.gpio_pin, 0)  
        GPIO.cleanup()
    
    def set_number(self, number):
        number = max(0, min(100, number))
        self.pwm.ChangeDutyCycle(number)

    def set_voltage(self, voltage):
        voltage = max(0, min(self.dynamic_range, voltage))  
        duty_cycle = (voltage / self.dynamic_range) * 100
        print(duty_cycle)
        self.set_number(duty_cycle)


if __name__ == "__main__":
    try:
        dac = PWM_DAC(12, 1000, 3.14, True)
        
        while True:
            try:
                voltage = float(input("Введите напряжение в вольтах (0-3.14): "))
                dac.set_voltage(voltage)
                print(f"Установлено напряжение: {voltage} В")
            except ValueError:
                print("Вы ввели не число. Попробуйте еще раз\n")
            except KeyboardInterrupt:
                print("\nПрограмма прервана пользователем")
                break
    finally:
        dac.deinit()