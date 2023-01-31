c = 0
for N in range(1, 1001):
    k = bin(N) [2:]
    if k.count('1') % 2 == 0:
        if k[0] == '1':
            k = k[1:]
    else:
        k = k.replace('0', '') + '1'
    if k.count('1') % 2 == 0:
        if k[0] == '1':
            k = k[1:]
    else:
        k = k.replace('0', '') + '1'
    r = int(k, 2)
    if r == 7:
        c += 1
print(c)