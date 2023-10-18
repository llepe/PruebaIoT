from pathlib import Path
is_rpi = Path("/etc/rpi-issue").exists()

if (not is_rpi):
    from tkgpio import TkCircuit

    # initialize the circuit inside the GUI

    configuration = {
        "width": 300,
        "height": 200,
        "leds": [
            {"x": 50, "y": 40, "name": "Amarillo", "pin": 21},
            {"x": 100, "y": 40, "name": "Rojo", "pin": 22}
        ]
    }

    circuit = TkCircuit(configuration)
    #@circuit.run
#########
def main ():
    
    # now just write the code you would use on a real Raspberry Pi
    
    from gpiozero import LED, Button
    from time import sleep
    import psutil
    
    ledAmarillo = LED(21)
    ledRojo = LED(22)

    print ("Inicio")

    while True:
        porcentaje = psutil.cpu_percent()
        print(porcentaje)
        if porcentaje < 10:
            print ("Esta bien")
            ledAmarillo.off()
            ledRojo.off()
        elif porcentaje < 20:
            print ("Alerta: CPU con carga media")
            ledAmarillo.on()
            ledRojo.off()
        else:
            ledAmarillo.on()
            ledRojo.on()
            print ("Emergencia: CPU con carga ALTA")
        sleep(.5)

    print ("Fin")
########
if (not is_rpi):
    circuit.run(main)
else:
    main()








