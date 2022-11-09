
# Programa de combinatoria
def factorial(a):
    f=1
    for i in range(1,a+1):
        f=f*i
    return f
    
n=int(input("Tamaño del conjunto: "))
m=int(input("Tamaño del grupo a crear: "))
nf=factorial(n)
mf=factorial(m)
nmf=factorial(n-m)
c=nf/(mf*nmf)
print(f"La cantidad de combinaciones es {c}")