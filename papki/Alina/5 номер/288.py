c=set()
for x in range(1,1000):
    n=bin(x)[2:]
    if x%2==0:
        n='1'+n+'10'
    else:
        n='11'+n+'0'
    r=int(n,2)
    if 800<=r<=1500:
        c.add(r)
print(len(c))        