c=0
for n in range(100,201):
    x=bin(n)[2:]
    if len(x)%2==0:
        x=x+'10'
    else:
        x='11'+x
    r=int(x,2)
    if r%2==0:
        c+=1
print(c)