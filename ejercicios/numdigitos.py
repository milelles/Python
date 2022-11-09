# """ Dado un numero cualquiera el programa muestra la cantidad de cifras que tiene """

n=float(input('ingrese un numero: '))
conteo=0
while n>0:
    if n%4==0:
        n=n//10
        continue
    n=n//10
    conteo+=1
print(f'el numero tiene {conteo} cifras ')
