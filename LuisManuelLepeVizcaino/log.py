from datetime import datetime

def escribe(strTexto):
    archivoLog = open("log.txt", "a")
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print(dt_string + ": "  + strTexto)
    archivoLog.write(dt_string + ": "  + strTexto)
    archivoLog.write("\r\n")
    archivoLog.close()