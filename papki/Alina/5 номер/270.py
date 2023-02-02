for x in range(1,1000):
    n=bin(x)[2:]
    if x%2==0:
        n='1'+n+'00'
    else:
        n='10'+n+'11'
    r=int(n,2)
    if r>1023:
        print(r)
        break