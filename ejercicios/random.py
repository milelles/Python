# "Programa que imprime 10 numeros random de 100 a 130, en orden par e impar"
import random
import os 
def numaleatorios():
    z=random.randint(100,130)
    while z==110 or z==115 or z==120:
        z=random.randint(100,130)
    return z 
x=numaleatorios()
#print(x) 
   
def numeros():
    os.system('cls')
    i=0
    for i in range(5):
        while i<6:
            p=numaleatorios()
            
            if p % 2 == 0:
                print(p)
                break
            else:
                continue
        while i<6:
            p=numaleatorios()
            if p%2!=0:
                print(p)
                break
            else:
                continue

   

numeros()
