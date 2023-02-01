c=0
for i in range(1,1000):
    n=bin(i)[2:]
    if n.count('1')%2==0:
        n=n[1:]
    else:
        n='1'*n.count('1')+'1'
    if n.count('1')%2==0:
        n=n[1:]
    else:
        n='1'*n.count('1')+'1'
    r=int(n,2)
    if r==7:
        c+=1
print(c)