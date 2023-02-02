a1=[]
for x in range(1,1000):
    n=bin(x)[2:]
    if x%2==0:
        n='11'+n+'11'
    else:
        n='1'+n+'0'    
    r=int(n,2)
    if r<126:
        a1.append(r)
print(max(a1))