import os
def entero(x):
    for i in range(len(x)):
        x[i]=int(x[i])
    return x
def orden(x):
    m=min(x)
    mp=x.index(m)
    mx=max(x)
    mxp=x.index(mx)
    orden=[mp,m,mxp,mx]
    return orden
def format(x):
    p="{:.2f}".format(x)
    return p
os.system('cls')
a=input()
b=a.split()
d=entero(b)
tipos=[]
while True:
    if b[0]<1:
        a=input()       #sucursales, #tipos, #pacientes
        b=a.split()
        d=entero(b)
        continue
    else:
        for i in range(b[0]):
            m=input()
            mt=m.split()
            entero(mt)
            tipos.append(mt)     
        break
pacientes=[] 
ent=[] #para guardar la suma
for i in range(b[0]):
    filas=[]
    for j in range (b[1]):
        filas.append(0)
    ent.append(filas)
contador=[]
for i in range(b[0]):
    contador.append(0)
for i in range(b[2]): #ciclo para ingresar datos por paciente
    p=input()
    pac=p.split() #datos por paciente 
    entero(pac)
    pacientes.append(pac)
    contador[pac[0]-1]+=1
    if pac[3]<72 and pac[4]<65: #hipotension
        ent[pac[0]-1][pac[1]-1]+=pac[2]
        tipos[pac[0]-1][pac[1]-1]-=pac[2]
    elif 72<=pac[3]<107 and 65<=pac[4]<73: #optima
        ent[pac[0]-1][pac[1]-1]+=0
        tipos[pac[0]-1][pac[1]-1]-=0
    elif 107<=pac[3]<124 and 73<=pac[4]<81: #normal
        ent[pac[0]-1][pac[1]-1]+=0
        tipos[pac[0]-1][pac[1]-1]-=0
    elif 124<=pac[3]<138 and 81<=pac[4]<93: #prehipertension
        ent[pac[0]-1][pac[1]-1]+=pac[2]
        tipos[pac[0]-1][pac[1]-1]-=pac[2]
    elif 138<=pac[3]<156 and 93<=pac[4]<102: #hta grado 1
        ent[pac[0]-1][pac[1]-1]+=pac[2]
        tipos[pac[0]-1][pac[1]-1]-=pac[2]
    elif 156<=pac[3]<175 and 102<=pac[4]<114: #hta grado 2
        ent[pac[0]-1][pac[1]-1]+=pac[2]
        tipos[pac[0]-1][pac[1]-1]-=pac[2]
    elif 175<=pac[3] and 114<=pac[4]: #hta grado 3
        ent[pac[0]-1][pac[1]-1]+=pac[2]
        tipos[pac[0]-1][pac[1]-1]-=pac[2]
    elif 136<=pac[3] and 92>pac[4]: #hipertension sistolica aislada
        ent[pac[0]-1][pac[1]-1]+=pac[2]
        tipos[pac[0]-1][pac[1]-1]-=pac[2]
    else:       
        ent[pac[0]-1][pac[1]-1]+=0
        tipos[pac[0]-1][pac[1]-1]-=0
medR=[]
for i in range(b[0]):
    fila=[]
    for j in range(b[1]):
        c=tipos[i][j]+ent[i][j]    
        fila.append(c)
    medR.append(fila)
for i in range(b[0]):
    print(i+1)
    ot=orden(tipos[i])
    print(ot[0]+1,ot[1])
    print(ot[2]+1,ot[3])
    oe=orden(ent[i])
    promedio=sum(ent[i])/b[1] #promedio con tipos de medicamentos
    prm=0  #promedio con pacientes atendidos
    if contador[i]==0:
        prm=0
    else:
        prm=sum(ent[i])/contador[i]    
    print(format(oe[1]),format(promedio),format(oe[3]))
    print(format(prm))
medicamento1=[]
for i in range(len(ent)):
    medicamento1.append(ent[i][0])
o1=orden(medicamento1)
print(o1[0]+1,o1[1])
print(o1[2]+1,o1[3])
    



