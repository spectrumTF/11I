for i in range(1000):
    n=bin(i)[2:]
    if i%2!=0:
        n='2'+n+'11'
    else:
        n='13'+n+'02'
    r=int(n,4)
    if r>1000:
        print(r)
        break
    
# работает
