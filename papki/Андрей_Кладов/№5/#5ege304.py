for n in range(1000,10000):
    x=hex(n)[2:]
    if n%2==0:
        x=x+'F'
    else:
        x=x+'0'
    x1=x
    f=0
    while x1!='':
        f+=int(x1[-1:],16)
        x1=x1[:-1]
    x=x+hex(f%16)[2:]
    x1=x
    f=0
    while x1!='':
        f+=int(x1[-1:],16)
        x1=x1[:-1]
    x=x+hex(f%16)[2:]
    r=int(x,16)
    ma=max(x)
    mi=min(x)
    if x.count(ma)*5==x.count(mi):
        print(n)
        break