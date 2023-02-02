c=0
for x in range(1,2000):
    n=bin(x)[2:]
    if x%2==0:
        n='1'+n+'11'
    else:
        n='11'+n+'0'
    r=int(n,2)
    if 500<=r<=1000:
        c+=1
print(c)