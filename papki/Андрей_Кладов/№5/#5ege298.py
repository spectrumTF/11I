c=0
for n in range(1,1000):
    x=bin(n)[2:]
    if x.count('1')%2==0:
        x=x[1:]
    else:
        x='1'*x.count('1')+'1'
    if x.count('1')%2==0:
        x=x[1:]
    else:
        x='1'*x.count('1')+'1'
    r=int(x,2)
    if r==7:
        c+=1
print(c)