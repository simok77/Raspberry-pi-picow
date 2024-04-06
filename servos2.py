from machine import Pin, PWM
import time

servo = PWM(Pin(0))
servo.freq(50)
Boton0 = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_DOWN)
Boton180 = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    if Boton0.value() == 1:
        servo.duty_u16(1311)
        time.sleep(0.5)
    if Boton180.value() == 1:
        servo.duty_u16(7864)
        time.sleep(0.5)