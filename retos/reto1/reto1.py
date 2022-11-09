alt=float(input())
temp=float(input())
if 400<=alt<=800 and 25<=temp<=28:
  print("SUMAMENTE APTO")
elif ((alt<400) or (801<=alt<=999) or (400<=alt<=800 )) and ((29<=temp<=30) or (21<=temp<=24) or (25<=temp<=28)):
    print("MODERADAMENTE APTO")
elif ((1000<=alt<=1200)or (400<=alt<=800) or (alt<400) or (801<=alt<=999) ) and ((31<=temp<=32) or (18<=temp<=20)or (25<=temp<=28)or (29<=temp<=30) or (21<=temp<=24)):
    print("MARGINALMENTE APTO")
elif ((alt<400) or (801<=alt<=999) or (400<=alt<=800 )or (1000<=alt<=1200)or (1200<alt)) and ((temp<18) or (32<temp) or (25<=temp<=28) or (29<=temp<=30) or (21<=temp<=24) or (31<=temp<=32) or (18<=temp<=20)):
    print("NO APTO")

