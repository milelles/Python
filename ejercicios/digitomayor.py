# """ Programa para la obtencion del digito mayor en un numero de 4 digitos ingresado por pantalla """

a=int(input("Ingrese un numero de 4 digitos: "))
if a>=1000 and a>=9999:
    mayor=0
    d1=a%10
    a=a//10
    d2=a%10
    a=a//10
    d3=a%10 
    a=a//10
    d4=a%10
    if d1>=mayor:
        mayor=d1
        if d2>=mayor:
            mayor=d2
        else:
            mayor=mayor
        if d3>=mayor:
                mayor=d3
        else:
                mayor=mayor
        if d4>=mayor:
                    mayor=d4
        else:
                    mayor=mayor
    if mayor%2==0:
        print(f"El numero mayor es {mayor} y es par")
    else:
        print(f"El numero mayor es {mayor} y es impar")
else:

     print("El numero debe ser de 4 digitos")