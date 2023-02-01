c=0
for n in range(1000):
    x=bin(n) [2:]
    if n%2==0:
        x='1'+x+'11'
    else:
        x='11'+x+'0'
    r=int(x,2)
    if 500<=r<=1000:
        c+=1
print(c)