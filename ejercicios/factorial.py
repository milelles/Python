
n=0
while n>=0:
    n=int(input("Ingrese un numero: "))
    if n==-1:
        break
    elif n==0:
        print(f"El factorial de {n} es 1")
        continue
    elif n<0:   
        n=-1*n   
        print("No se ha definido factorial de numeros negativos")
        continue
    else:
        c=1    
        for i in range(1,n+1):
            c=c*i
    print(f"El factorial de {n} es {c}")        
    
print("Fin del proceso")
