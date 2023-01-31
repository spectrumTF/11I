b = []
for N in range(2, 1000):
    k = bin(N) [2:]
    k = k[1:]
    k = str(round(int(k)))
    if k.count('1') % 2 == 0:
        k = '10' + k
    else:
        k = '1' + k + '0'
    r = int(k, 2)
    if r < 450:
        b.append(r)
print(max(b))