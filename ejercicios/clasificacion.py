# Programa que pide por pantalla 10 numeros y clasifica la cantidad de positivos, negativos y netros que hay
pos=0
neg=0
neu=0
positivos="{"
negativos="{"
for i in range(10):
    n=int(input("Ingrese un numero: "))
    if n==0:
        neu+=1
    elif n<0:
        neg+=1
        negativos= negativos + str(n) + ' '
    else:
        pos+=1
        positivos=positivos +str (n) + ' '
negativos= negativos + "}"
positivos= positivos + "}"
print(f"Hay {pos} numeros positivos que son {positivos}")
print(f"Hay {neg} numeros negativos que son {negativos}")
print(f"Hay {neu} numeros neutros")