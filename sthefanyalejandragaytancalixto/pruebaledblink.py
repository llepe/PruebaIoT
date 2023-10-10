from tkgpio import TkCircuit

configuration = {
    "width": 300,
    "height": 200,
    "leds": [
        {"x": 50, "y": 40, "name": "LED 1", "pin": 21},
    ],
}

circuit = TkCircuit(configuration)
@circuit.run
def main ():
    
    from gpiozero import LED, Button
    from time import sleep
    
    led1 = LED(21)
    led1.blink()