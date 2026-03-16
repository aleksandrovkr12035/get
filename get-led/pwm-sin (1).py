import pwm_dac as pw
import signal_generator as sg
import time

amplitude = 3
signal_frequency = 15
sampling_frequency = 1000
t=0


try:
    p=pw.PWM_DAC(12, 1000, 3.28, True)
    while True:
        d=sg.get_sin_wave_amplitude(signal_frequency, t)*amplitude
        print(d)
        p.set_voltage(d)
        sg.wait_for_sampling_period(sampling_frequency)
        t+=1/sampling_frequency
finally:
    p.deinit()