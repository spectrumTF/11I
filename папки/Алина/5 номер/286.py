for x in range(1,1000):
    n=bin(x)[2:]
    if x%2==0:
        n+='10'
    else:
        n='1'+n+'01'
    r=int(n,2)
    if r>420:
        print(x)
        break