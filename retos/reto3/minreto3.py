
inventario = []
while True:
    leer = input().split()
    n = int(leer[0])
    m = int(leer[1])
    if n < 1:
        continue
    while True:
        leer = int(input())
        if leer >= 1:
            inventario.append(leer)
            if len(inventario) == n:
                break
        else:
            inventario.clear()
    break        
dosis = [0]*n
for j in range(m):
    pacientes = input().split()
    if int(pacientes[1]) < 72 and int(pacientes[2]) < 65:
        dosis[int(pacientes[0])-1] = dosis[int(pacientes[0])-1] + 4
    elif (int(pacientes[1]) >= 124 and int(pacientes[1]) < 138) and (int(pacientes[2]) >= 81 and int(pacientes[2]) < 93):
        dosis[int(pacientes[0])-1] = dosis[int(pacientes[0])-1] + 2
    elif (int(pacientes[1]) >= 138 and int(pacientes[1]) < 156) and (int(pacientes[2]) >= 93 and int(pacientes[2]) < 102):
        dosis[int(pacientes[0])-1] = dosis[int(pacientes[0])-1] + 4
    elif (int(pacientes[1]) >= 156 and int(pacientes[1]) < 175) and (int(pacientes[2]) >= 102 and int(pacientes[2]) < 114):
        dosis[int(pacientes[0])-1] = dosis[int(pacientes[0])-1] + 8
    elif int(pacientes[1]) >= 175 and int(pacientes[2]) >= 114:
        dosis[int(pacientes[0])-1] = dosis[int(pacientes[0])-1] + 16
    elif int(pacientes[1]) >= 136 and int(pacientes[2]) < 92:
        dosis[int(pacientes[0])-1] = dosis[int(pacientes[0])-1] + 12
    else:
        dosis[int(pacientes[0])-1] = dosis[int(pacientes[0])-1] + 0
postInventario = [0]*n
for i in range(n):
    postInventario[i] = inventario[i] - dosis[i]
print(postInventario.index(min(postInventario))+1, min(postInventario))
print(postInventario.index(max(postInventario))+1, max(postInventario))
for i in range(n):
    porcentaje = '{:.2f}'.format((dosis[i]/inventario[i])*100)
    print(f'{i+1} {porcentaje}%')