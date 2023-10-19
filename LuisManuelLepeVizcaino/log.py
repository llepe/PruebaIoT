from datetime import datetime

def escribe(strTexto):
    archivoLog = open("log.txt", "a")
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print(dt_string + ": "  + strTexto)
    archivoLog.write(dt_string + ": "  + strTexto)
    archivoLog.write("\r\n")
    archivoLog.close()

def lee():
    archivoLog = open("log.txt", "r")
    for x in range(3):
        linea = archivoLog.read()
        print (linea)
    archivoLog.close()    
