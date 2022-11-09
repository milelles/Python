# "Programa para la suma de productos en un supermarket"
def producto(n,m):
    print(n," ",m)
    
def caja():
    suma=0
    p="s"
    while p=="s":
        n=input("ingrese producto: ")
        m=int(input("Ingrese precio: "))
        suma+=m
        producto(n,m)
        p=input("Tiene mas productos? (s/n): ")
        #if p=="s":
        #    continue
        #else:
         #   print(f"El total de sus productos es: {suma}")
    print(f"El valor total es: {suma}")     
    return suma     



