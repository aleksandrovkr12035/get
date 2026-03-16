import r2r_dac as r2r
import signal_generator as sg
import time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000
t = 0

try:
    dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.124, True)
    while True:
        voltage = sg.get_sin_wave_amplitude(signal_frequency, t) * amplitude
        dac.set_voltage(voltage)
        sg.wait_for_sampling_period(sampling_frequency)
        t += 1/sampling_frequency
        if t > 1:  
            t = 0
finally:
    if hasattr(dac, 'deinit'):
        dac.deinit()