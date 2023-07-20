import sys

if len(sys.argv) == 4:
    value = 0
    for i in sys.argv:
        print( i, " es el parametro numero ", value)
        value+=1
else:
    raise ValueError("debes ingresar 3 argumentos")