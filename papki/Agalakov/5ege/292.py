for i in range(10000):
    n = bin(i)[2:]
    if n.count('1')%2==0:
        n = '10' + n[2:] + '1'
    else:
        n = '11' + n[2:] + '1'
    r = int(n,2)
    if r<35:
        print(i)

