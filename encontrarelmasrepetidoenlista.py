def masrepetido(lista):
    contador = {}
    for i in lista:
        if i in contador:
            contador[i] +=1
        
        if not (i in contador):
            contador[i] = 1
            
    print(contador)
    nrepeticionesmax = 0
    elmasrepetido = None
    for numero, repeticiones in contador.items():
        if repeticiones > nrepeticionesmax:
            nrepeticionesmax = repeticiones
            elmasrepetido = numero
    print(f"el numero mas repetido es el {elmasrepetido} que se repite {nrepeticionesmax} veces")
    return nrepeticionesmax, elmasrepetido
        
lista = [1,1,5,6,8,10,22,5,6,4,11,9,5]
masrepetido(lista)