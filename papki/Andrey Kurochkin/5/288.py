c=0
for i in range(1,10000):
    n=bin(i)[2:]
    if i%2==0:
        n='1'+n+'10'
    else:
        n='11'+n+'0'
    r=int(n,2)
    if r>=800 and r<=1500:
        c+=1
print(c)