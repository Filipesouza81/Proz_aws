numero=0
for i in range(21):
    numero=numero+1
    if(numero==13):
        continue
    if(numero==21):
        break
    print(numero)


numero=21
for i in range(21,1,-1):
    numero=numero-1
    if(numero==13):
        continue
    if(numero==0):
        break
    print(numero)


for i in range(13):
    print(i)
for i in range(14,21):
    print(i)