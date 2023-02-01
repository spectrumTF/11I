for n in range(1,10000):
    x1=bin(n)[2:]
    n1=n-int(x1.count('0'))
    x=bin(n1)[2:]
    x=x[-3:]+x
    r=int(x,2)
    if r>224:
        print(r)
        break