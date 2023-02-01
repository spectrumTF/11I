c=[]
for n in range(1000):
    x=bin(n)[2:]
    if n%2==0:
        x='1'+x+'10'
    else:
        x='11'+x+'0'
    r=int(x,2)
    if 800<=r<=1500:
        c.append(r)
print(len(set(c)))