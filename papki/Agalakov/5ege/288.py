a =[]
for i in range(10000):
    n = bin(i)[2:]
    if int(n)%2==0:
        n = '1' + n + '10'
    else:
        n = '11' + n + '0'
    r = int(n,2)
    if r<=1500 and r>=800:
        a.append(r)
print(len(set(a)))
