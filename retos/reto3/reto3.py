#ambos programas hacen lo mismo solo es un una variacion
import os
os.system('cls')
a=input()
b=a.split()
b[0]=int(b[0])
b[1]=int(b[1])
med=[] #medicamentos que quedan en sucursal
ent=[0]*b[0] #para guardar la suma
medR=[] #guardar lote de med real
while True:
    if b[0]<1:
        a=input()
        b=a.split()
        b[0]=int(b[0])
        b[1]=int(b[1])
        continue
    else:
        for i in range(b[0]):
            m=int(input())
            if m<=1:
                m=int(input())
            else:
                med.append(m)
                medR.append(m)
        break
for i in range(b[1]):
    pac=input()
    p=pac.split()
    p[0]=int(p[0])
    p[1]=int(p[1])
    p[2]=int(p[2])
    if p[1]<72 and p[2]<65:
        med[p[0]-1]-=4
        ent[p[0]-1]+=4
    elif 72<=p[1]<107 and 65<=p[2]<73:
        med[p[0]-1]-=0
        ent[p[0]-1]+=0
    elif 107<=p[1]<124 and 73<=p[2]<81:
        med[p[0]-1]-=0
        ent[p[0]-1]+=0  
    elif 124<=p[1]<138 and 81<=p[2]<93:
        med[p[0]-1]-=2
        ent[p[0]-1]+=2
    elif 138<=p[1]<156 and 93<=p[2]<102:
        med[p[0]-1]-=4
        ent[p[0]-1]+=4
    elif 156<=p[1]<175 and 102<=p[2]<114:
        med[p[0]-1]-=8
        ent[p[0]-1]+=8
    elif 175<=p[1] and 114<=p[2]:
        med[p[0]-1]-=16
        ent[p[0]-1]+=16
    elif 136<=p[1] and 92>p[2]:
        med[p[0]-1]-=12
        ent[p[0]-1]+=12
c=min(med)
d=med.index(c)
e=max(med)
f=med.index(e)
print(d+1,c)
print(f+1,e)
for i in range(b[0]):
    porcentaje=(ent[i]/medR[i])*100
    cal="{:.2f}".format(porcentaje)
    print(f"{i+1} {cal}%")

