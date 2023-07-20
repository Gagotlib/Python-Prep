import sys
import datetime
if len(sys.argv) == 4:
    marcadetiempo = datetime.datetime.now()
    print(marcadetiempo)
    marcadetiempo2 = int(datetime.datetime.timestamp(marcadetiempo))
    print(marcadetiempo2)

    temperatura = sys.argv[1]
    humedad = sys.argv[2]
    lluvia = sys.argv[3]

    print("temperatura:", temperatura, " humedad: ", humedad, " llovio: ", lluvia)
    marcadetiempo2 = str(marcadetiempo2)
    temperatura = str(temperatura)
    humedad = str(humedad)
    lluvia = str(lluvia)
    linea =  marcadetiempo2 + "," + temperatura + "," + humedad + "," +lluvia

    log = open('clase09_ej20.csv', 'a')
    log.write(linea + "\n")
    log.close()



else:
    print("numero de argumentos invalido")
    print("ingresar 4 argumentos:")
    print("nombre archivo - temperatura - humedad - lluvia")