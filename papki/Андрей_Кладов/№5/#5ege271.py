for N in range(1,1000):
    n= bin(N)[2:]
    if N%2!=0:
        n = '10' + n + '11'
    else:
        n = '1' + n + '10'
    r=int(n,2)
    if r>1023:
        print(r)
        break