m=0
for i in range(1,10000):
    n = bin(i)[2:]
    if int(n)%2!=0:
        n = '1' + n + '00'
    else:
        k = n.count('1')
        g = bin(k)[2:]
        n = n + g
    r = int(n,2)
    if r>=500 and r<=700:
        m+=1
print(m)
