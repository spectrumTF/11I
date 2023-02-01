for i in range(1000):
    n=bin(i)[2:]
    if i%2!=0:
        n='10'+n+'11'
    else:
        n='1'+n+'00'
    r=int(n,2)
    if r>1023:
        print(r)
        break