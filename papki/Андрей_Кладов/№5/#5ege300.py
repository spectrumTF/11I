ma=0
for n in range(1,1000):
    x=bin(n)[3:]
    if x.count('1')%2==0:
        x='10'+x
    else:
        x='1'+x+'0'
    r=int(x,2)
    if r<450 and r>ma:
        ma=r
print(ma)