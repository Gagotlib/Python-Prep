ciclos = 0
n = 0
primo = True
tope_rango = 30

while (n < tope_rango):
    for div in range(2, n):
        ciclos += 1
        if (n % div == 0):
            primo = False
    if (primo):
        print(n)
    else:
        primo = True
    
    n+=1

print ("cantidad de siclos: ", str(ciclos))
