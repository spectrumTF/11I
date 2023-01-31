for N in range(1, 100):
    a = bin(N) [2:]
    if a.count('1') % 2 == 0:
        a = '10' + a[2:] + '0'
    else:
        a = '11' + a[2:] + '1'
    r = int(a, 2)
    if r < 35:
        print(N)