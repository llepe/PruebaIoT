from pathlib import Path
is_rpi = Path("/etc/rpi-issue").exists()

if (not is_rpi):
    from tkgpio import TkCircuit

    # initialize the circuit inside the GUI

    configuration = {
        "width": 500,
        "height": 150,
        "leds": [
            {"x": 50, "y": 40, "name": "LED", "pin": 21},
        ],
        "distance_sensors": [
            {"x": 150, "y": 40, "name": "Distance Sensor (cm)", "trigger_pin": 17, "echo_pin": 18, "min_distance": 5, "max_distance": 30}
    ]
    }

    circuit = TkCircuit(configuration)
    #@circuit.run
#########
def main ():
    
    # now just write the code you would use on a real Raspberry Pi
    
    from gpiozero import LED, Button, DistanceSensor
    from time import sleep
    import psutil
    import log

    led = LED(21)

    distance_sensor = DistanceSensor(trigger=17, echo=18)

    while True:
        distancia = distance_sensor.distance
        print(distancia * 100)
        if (distancia < .07):
            led.on()
        else:
            led.off()
        sleep(1)

########
if (not is_rpi):
    circuit.run(main)
else:
    main()








