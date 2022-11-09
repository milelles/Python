import os
os.system('cls')
def entero(x):
    for i in range(len(x)):
        x[i]=int(x[i])
    return x

nombre_archivo="data.csv"
with open(nombre_archivo,'r') as archivo:
    next(archivo,None)
    x=int(input())
    conM=0
    conH=0
    sumaT=0
    salida1=[0,0,0]
    for linea in archivo:
        linea=linea.rstrip()
        separador=","
        lista=linea.split(",")
        nombre=lista[0]
        apellido=lista[1]
        genero=lista[2]
        ciudad=lista[3]
        departamento=lista[4]
        sucursal=int(lista[5])
        medtipo=int(lista[6])
        medcant=int(lista[7])
        psistolica=int(lista[8])
        pdistolica=int(lista[9])
        if sucursal==x:
            salida1[0]=x
            salida1[1]=ciudad
            salida1[2]=departamento
        if sucursal==x and psistolica<91 and pdistolica<63:  #hipotension
            if genero=="m":
                conH+=1
                sumaT+=medcant
            else:
                conM+=1
                sumaT+=medcant
        elif sucursal==x and 91<=psistolica<134 and 63<=pdistolica<77: #ideal
            if genero=="m":
                conH+=0
                sumaT+=0
            else:
                conM+=0
                sumaT+=0
        elif sucursal==x and 134<=psistolica<162 and 77<=pdistolica<105: #normal
            if genero=="m":
                conH+=0
                sumaT+=0
            else:
                conM+=0
                sumaT+=0
        elif sucursal==x and 162<=psistolica<188 and 105<=pdistolica<119: #normal-alta
            if genero=="m":
                conH+=1
                sumaT+=medcant
            else:
                conM+=1
                sumaT+=medcant
        elif sucursal==x and 188<=psistolica<201 and 119<=pdistolica<126: #hta-grado1
            if genero=="m":
                conH+=1
                sumaT+=medcant
            else:
                conM+=1
                sumaT+=medcant
        elif sucursal==x and 201<=psistolica<214 and 126<=pdistolica<146: #hta grado 2
            if genero=="m":
                conH+=1
                sumaT+=medcant
            else:
                conM+=1
                sumaT+=medcant
        elif sucursal==x and 214<=psistolica and 146<=pdistolica: #hta grado 3
            if genero=="m":
                conH+=1
                sumaT+=medcant
            else:
                conM+=1
                sumaT+=medcant
        elif sucursal==x and 152<=psistolica and 77>pdistolica: #hipertension solo sistolica
            if genero=="m":
                conH+=1
                sumaT+=medcant
            else:
                conM+=1
                sumaT+=medcant
    archivo.close()
promedio=sumaT/(conH+conM)
promedio="{:.2f}".format(promedio)
print(x,salida1[1],salida1[2])
print("scheduled patients")
print("male",conH)
print("female",conM)
print("total",conH+conM)
print("scheduled medicine quantity")
print("mean",promedio)
print("total",sumaT)
    


