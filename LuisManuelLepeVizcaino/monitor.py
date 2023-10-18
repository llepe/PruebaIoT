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
    import log

    ledAmarillo = LED(21)
    ledRojo = LED(22)

    log.escribe("Inicio")
    
    while True:
        porcentaje = psutil.cpu_percent()
        log.escribe(str(porcentaje))
        if porcentaje < 10:
            log.escribe("Esta bien")
            ledAmarillo.off()
            ledRojo.off()
        elif porcentaje < 20:
            log.escribe("Alerta: CPU con carga media")
            ledAmarillo.on()
            ledRojo.off()
        else:
            log.escribe("Emergencia: CPU con carga ALTA")
            ledAmarillo.on()
            ledRojo.on()
        sleep(.5)

    log.escribe("Fin")
########
if (not is_rpi):
    circuit.run(main)
else:
    main()








