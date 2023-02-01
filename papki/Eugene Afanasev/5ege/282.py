for n in range(10000,1,-1):
    x=bin(n)[2:]
    if n%2==0:
        l=x.count('1')
        o=bin(l)[2:]
        x=x+o
    else:
        x='1'+x+'00'
    r=int(x,2)
    if r<1000:
        print(n)
        break