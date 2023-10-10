from gpiozero import led
from time import sleep

led = LED(14)

while True:
    led.on(1)
    sleep(1)
    led.off(1)
    sleep(1)