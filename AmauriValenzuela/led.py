from tkgpio import TkCircuit
from pathlib import Path
is_rpi = Path("/etc/rpi-issue").exists()

# initialize the circuit inside the GUI
if not is_rpi:
    from tkgpio import TkCircuit

configuration = {
    "width": 300,
    "height": 200,
    "leds": [
        {"x": 50, "y": 40, "name": "LED 1", "pin": 15},
    ],
    "buttons": [
        {"x": 50, "y": 130, "name": "Press to toggle LED 2", "pin": 11},
    ]
}
    # initialize the circuit inside the GUI

circuit = TkCircuit(configuration)
@circuit.run
    configuration = {
        "width": 300,
        "height": 200,
        "leds": [
            {"x": 50, "y": 40, "name": "LED 1", "pin": 15},
        ],
        "buttons": [
            {"x": 50, "y": 130, "name": "Press to toggle LED 2", "pin": 11},
        ]
    }

    circuit = TkCircuit(configuration)
#@circuit.run

def main ():

if is_rpi:
    main()
else:
    circuit.run(main)
