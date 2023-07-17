class Herramientas2:
    def __init__(self, listavalores):
        self.listavalores = listavalores 

    def convertir_grados(self, origen, destino):
        for i in self.listavalores:
            print(i,"grados", origen, "son",self.__convertir_grados(i,origen,destino), "grados", destino)

    def __convertir_grados(self, valor, origen, destino):
        if origen == "Celsius" and destino == "Farenheit":
            valor_destino = (valor * 9/5) +32
        elif origen == "Celsius" and destino == "Kelvin":
            valor_destino = valor + 273.15
        elif origen == "Celsius" and destino == "Celsius":
            valor_destino = valor
        elif origen == "Farenheit" and destino == "Celsius":
            valor_destino = (valor -32) * 5/9
        elif origen == "Farenheit" and destino == "Kelvin":
            valor_destino = ((valor - 32) * 5/9) + 273.15
        elif origen == "Farenheit" and destino == "Farenheit":
            valor_destino = valor
        elif origen == "Kelvin" and destino == "Celsius":
            valor_destino = valor - 273.15
        elif origen == "Kelvin" and destino == "Farenheit":
            valor_destino = (valor - 273.15) *9/5 + 32
        elif origen == "Kelvin" and destino == "Kelvin":
            valor_destino = valor
        else:
            return "unidades no validas"
        return valor_destino
        

    def masrepetido(self, listavalores):
        contador = {}
        for i in listavalores:
            if i in contador:
                contador[i] +=1
        
            elif not (i in contador):
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

    def encontrarprimo(self):
        for i in self.listavalores:
            if (self.__encontrarprimo(i)):
                return print(i,"es primo")
            else:
                return print(i,"no es primo")
        
                
    
    def __encontrarprimo(self,nro):
        primo = True
        for div in range(2, nro):
            if (nro % div == 0):
                primo = False
        if (primo):
            return primo
        else:
            return False
        
