c=0
for n in range(1000,10000):
    x=str(n)
    if int(x[0])%2==0:
        if int(x[1])-int(x[3])<0:
            r=int(x[0])+int(x[2])-(int(x[1])-int(x[3]))
        else:
            r=int(x[0])+int(x[2])+(int(x[1])-int(x[3]))
    else:
        x=sorted(x)
        x=''.join(x)
        x=int(x)
        x=bin(x)[2:]
        r=x.count('1')
    if r>20:
        c+=1
print(c)