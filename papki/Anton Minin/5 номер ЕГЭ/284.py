for i in range(500,700):
    n=bin(i)[2:]
    if i%2==0:
        n=n+bin(int(n.count('1')))[2:]
    else:
        n='1'+n+'00'
    r=int(n,2)
    print(r)
        
