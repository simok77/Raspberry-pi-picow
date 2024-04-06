from machine import Pin, PWM
import time

servo = PWM(Pin(0))
servo.freq(50)

while True:
    servo.duty_u16(1311)
    time.sleep(2)
    print("Lado 1")
    servo.duty_u16(7864)
    time.sleep(2)
    print("Lado 2")
    