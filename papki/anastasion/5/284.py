c=0
for i in range(10000):
    n=bin(i)[2:]
    if i%2==0:
        s=n.count('1')
        n=n+bin(s)[2:]
    else:
        n='1'+n+'00'
    r=int(n,2)
    if 500<=r<=700:
        c+=1
print(c)
    
