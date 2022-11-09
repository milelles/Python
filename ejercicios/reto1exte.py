alt=float(input("ingrese altura: "))
temp=float(input("ingrese temperatura: "))
if (1200<alt) or (temp<18 or 32<temp):
    print("NO APTO")
elif (1000<=alt<=1200) or (31<=temp<=32 or 18<=temp<=20):
    print("MARGINALMENTE APTO")
elif (alt<400 or 801<=alt<=999) or (29<=temp<=30 or 21<=temp<=24):
    print("MODERADAMENTE APTO")
elif 400<=alt<=800 or 25<=temp<=28:
  print("SUMAMENTE APTO")
