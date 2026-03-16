import RPi.GPIO as GPIO

class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose=False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial=0)
    
    def deinit(self):
        GPIO.output(self.gpio_bits, [0] * len(self.gpio_bits)) 
        GPIO.cleanup()
    
    def set_number(self, number):
        binary = bin(number)[2:].zfill(8)
        values = [int(bit) for bit in binary]  
        GPIO.output(self.gpio_bits, values)
        
        if self.verbose:
            print(f"Установлено число: {number} -> биты: {binary}")
    
    def set_voltage(self, voltage):

        if voltage < 0:
            voltage = 0
        elif voltage > self.dynamic_range:
            voltage = self.dynamic_range
            

        number = int(voltage / self.dynamic_range * 255)
        self.set_number(number)

if __name__ == "__main__":
    try:
        dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.124, True)
        
        while True:
            try:
                voltage = float(input("Введите напряжение в вольтах (0-3.124): "))
                dac.set_voltage(voltage)
            except ValueError:
                print("Вы ввели не число. Попробуйте еще раз\n")
            except KeyboardInterrupt:
                break
    finally:
        dac.deinit()
