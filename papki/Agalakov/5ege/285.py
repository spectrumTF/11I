m = []
for i in range(1,1000):
    n = bin(i)[2:]
    if int(n)%2==0:
        n = n + '10'
    else:
        n = '1' + n + '01'
    r = int(n,2)
    if r>516:
        m.append(i)
print(min(m))
