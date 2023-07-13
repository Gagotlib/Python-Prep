def convertir_grados(valor, origen, destino):
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