for N in range(1, 100):
    k = bin(N) [2:]
    if k.count('1') % 2 == 0:
        if k[0] == '1': 
            k = k[1:]
        k = str(round(int(k)))
    else:
        k = '1' + str(k) + '00'

    if k.count('1') % 2 == 0:
        if k[0] == '1': 
            k = k[1:]
        k = str(round(int(k)))
    else:
        k = '1' + k + '00'
    r = int(k, 2)
    if r > 100:
        print(N)
        break