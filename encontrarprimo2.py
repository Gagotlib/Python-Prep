n = 0
primo = True

while n < 100:
    for x in range (2,n):
        if n % x == 0 :
            primo = False
        
    if (primo):
        print (n)
    n+=1
    primo = True
    
