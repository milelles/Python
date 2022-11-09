veces=int(input())
i=0
conteo1=0
conteo2=0
sum1=0
sum2=0
sumapto=0
moderadamente=0
marginalmente=0
noapto=0
while i<veces:
    alt=float(input())
    sum1=sum1+alt
    conteo1=conteo1+1
    temp=float(input())
    sum2=sum2+temp
    conteo2=conteo2+1
    if (1200<alt) or (temp<18 or 32<temp):
        noapto+=1
    elif (1000<=alt<=1200) or (31<=temp<=32 or 18<=temp<=20):
        marginalmente+=1
    elif (alt<400 or 801<=alt<=999) or (29<=temp<=30 or 21<=temp<=24):
        moderadamente+=1
    elif 400<=alt<=800 or 25<=temp<=28:
        sumapto+=1
    i=i+1
altura=sum1/conteo1
temperatura=sum2/conteo2
print("{:.2f}".format(altura))
print("{:.2f}".format(temperatura))
print(f"sumamente apto {sumapto}")
print(f"moderadamente apto {moderadamente}")
print(f"marginalmente apto {marginalmente}")
print(f"no apto {noapto}")
