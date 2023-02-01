ma=0
for N in range(1,1000):
    n=bin(N)[2:]
    if N%2!=0:
        n='1'+n+'11'
    else:
        n = '11' + n + '00'
    r=int(n,2)
    if r < 127 and r>ma :
        ma=r
print(ma)
