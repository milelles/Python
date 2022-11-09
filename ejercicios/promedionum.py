print("PROGRAMA DE PROMEDIO DE NUMEROS ALEATORIOS")
num=float(input("Ingrese un numero: "))
suma=num
conteo=1

while True: 
    num=float(input("Ingrese un numero: "))
    if num==-1:
        print(f"El promedio es {suma/conteo}")
    else:
         suma=suma+num
         conteo=conteo+1
  
