c=0
for n in range(1000,10000):
    x=str(n)
    if int(x[0])%4==0:
        x='9'+x[1:]
    if int(x[0])%2==0 and int(x[0])%4!=0:
        x='3'+x[1:]
    r=oct(int(x))[2:]
    if x[0]=='9' and r[-1:]=='4':
        c+=1
print(c)