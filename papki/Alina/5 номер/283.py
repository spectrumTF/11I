for x in range(1000,1,-1):
    n=bin(x)[2:]
    if x%2==0:
        n+=bin(n.count('1'))[2:]
    else:
        n='1'+n+'00'
    r=int(n,2)
    if r<1000:
        print(x)
        break