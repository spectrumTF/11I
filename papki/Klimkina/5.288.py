a=[]
for i in range(0,1000):
    n=bin(i)[2:]
    if i%2==0:
        n='1'+n+'10'
    else:
        n='11'+n+'0'
    r=int(n,2)
    if 800<=r<=1500:
        a.append(r)
print(len(set(a)))