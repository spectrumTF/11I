for N in range(1000, 10000):
    N = str(N)
    if int(N) % 2 == 0:
        k = sorted(N, reverse = True)
        R = int(''.join(k)) // 2
    if (R - int(N)) == 1:
        print(R)
        break
    else:
        k = sorted(N)
        R = int(''.join(k)) * 2
    if (R - int(N)) == 1:
        print(R)
        break