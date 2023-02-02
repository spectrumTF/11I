for x in range(1,1000):
    n=bin(x)[2:]
    if x%2==0:
        n+=bin(n.count('1'))[2:]
    else:
        n='1'+n+'00'
    r=int(n,2)
    if r>215:
        print(x)
        break