for i in range(0,1000):
    n=bin(i)[2:]
    if i%2==0:
        n=n+'10'
    else:
        n='1'+n+'01'
    r=int(n,2)
    if r>516:
        print(i)
        break