a=[]
for i in range(1, 1000):
    n=bin(i) [2:]
    if i%2!=0:
        n='1'+n+'11'
    else:
        n='11'+n+'00'
    r=int(n,2)
    if r<127:
        a.append(r)
print(max(a))