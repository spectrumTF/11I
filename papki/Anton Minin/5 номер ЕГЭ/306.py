c=0
for i in range(100,201):
    n=bin(i)[2:]
    if len(n)%2==0:
        n=n+'10'
    else:
        n='11'+n
    r=int(n,2)
    if r%2==0:
        c+=1
print(c)
        
    