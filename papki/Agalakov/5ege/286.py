for i in range(1000):
    n = bin(i)[2:]
    if int(n)%2==0:
        n = '10'+n+'1'
    else:
        n = '1'+n+'01'
    r = int(n,2)
    if r>420:
        print(i)
        break
