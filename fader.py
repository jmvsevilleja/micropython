# Fade In and Out

# import machine
from machine import Pin
from machine import PWM
import time


def fade():

    # Machine
    # print(machine.freq())
    # frequency must be 20MHz, 40MHz, 80Mhz, 160MHz or 240MHz
    # machine.freq(160000000)

    # Set our pin 2 to PWM
    pwm = PWM(Pin(2))

    # Frequency = 100hz
    pwm.freq(100)

    # Pulse effect
    # pwm.freq(1)
    # pwm.duty(512)

    # Print increment number
    # number = 0
    # while 1:
    #     number += 1
    #     print(number)
    #     time.sleep(1)

    while 1:
        # Brightness between 0 and 1023
        for brightness in range(0, 1023, 100):
            pwm.duty(brightness)
            # print(brightness)
            time.sleep(0.1)

        # Brightness between 1023 and 0
        for brightness in range(1023, 0, -100):
            pwm.duty(brightness)
            # print(brightness)
            time.sleep(0.1)
