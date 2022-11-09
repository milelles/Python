# "Programa para la obtencion de letras de una palabra ingresada por pantalla"
palabra=input("Ingrese su palabra: ")
k=0
for i in range(len(palabra)):
    if palabra[i]=="a":
        break
    k+=1
    print(str(i) + ' ' + palabra[i])
print(f"la palabra tiene {k} letras")