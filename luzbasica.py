from machine import Pin
import time
led = Pin ("LED",Pin.OUT)
while True:
    led.value (1)
    print("Paso 1")
    time.sleep (0.9)
    led.value (0)
    print("Paso 2")
    time.sleep (0.9)