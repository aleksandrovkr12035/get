import RPi.GPIO as GPIO


def voltage_to_number(voltage):
    if not (0.0 <= voltage <= 3.3):
        print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - 3.124 B)")
        print("устанавливаем 0.0 В")
        return 0

    return int(voltage / 3.124 * 255)

def number_to_dac(value):   
    return [int(element) for element in bin(value)[2::].zfill(8)]

dac_bits = [22, 27, 17, 26, 25, 21, 20, 16]
dac_bits = dac_bits[::-1]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac_bits, GPIO.OUT)


try:
    while True:
        try:
            voltage = float(input("введите напряжение в Ввольтах: "))
            number = voltage_to_number(voltage)
            GPIO.output(dac_bits, number_to_dac(number))

        except ValueError:
            print("вы ввели не число. попробуйте еще раз\n")

finally:
    GPIO.output(dac_bits, 0)
    GPIO.cleanup()
