l = 0
for i in range(10000):
    n = bin(i)[2:]
    if int(n)%2==0:
        n = '1' + n + '11'
    else:
        n = '11' + n + '0'
    r = int(n,2)
    if r<=1000 and r>=500:
        l+=1
print(l)
