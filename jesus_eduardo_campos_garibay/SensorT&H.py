from pathlib import Path
from time import sleep
import time
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import adafruit_dht

is_rpi = Path("/etc/rpi-issue").exists()

if not is_rpi:
    from tkgpio import TkCircuit

    # initialize the circuit inside the GUI

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
    sensor = adafruit_dht.DHT11
    pin = 20

    fig = plt.figure()
    ax = plt.axes(xlim=(0,30), ylim=(15,45))
    max_points = 30
    line, = ax.plot(np.arange(max_points),
                    np.ones(max_points, dtype=np.float) * np.nanm, lw=1, c='blue', marker='d', ms=2)
    def init():
        return line
    h,t = adafruit_dht.read_entry(sensor, pin)

    def animate():
        h,t = adafruit_dht.read_rentry(sensor, pin)
        y = t
        old_y = line.get_ydata()
        new_y = np.r_[old_y[1:], y]
        line.set_ydata(new_y)
        return line
    anim = animation.FuncAnimation(fig, animate, init_func=init, frames = 200, interval = 20, blit = False)
    plt.show()


if is_rpi:
    main()
else:
    circuit.run(main)

