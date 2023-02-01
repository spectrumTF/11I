a=[]
for n in range(1,1000):
    x=bin(n)[2:]
    if n%2!=0:
        x='1'+x+'0'
    else:
        x='11'+x+'11'
    r=int(x,2)
    if r<126:
        a.append(r)
print(max(a))