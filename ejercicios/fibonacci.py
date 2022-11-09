n=int(input("ingrese un numero: "))
x=0
y=1
serie= str(x) + " " +  str(y) + " "
if n==1:
    print(x)
elif n==2:
    print(f"{x}  {y} ")
else:
    for i in range(n-2):
      
        z=x+y
        serie= serie + str(z) + ' '
        x=y
        y=z  
    print(f"{serie}")
