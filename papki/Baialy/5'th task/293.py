N = 120
for M in range(10, 100000):
    k = M
    s = M
    p1 = 1
    p2 = 1
    while k:
        if k % 10 != 0:
            if (k % 10) % 2 == 0:
                p1 = p1 * (k % 10)
        k = k // 10
    p1 = p1 * 2
    while s:
        if s % 10 != 0:
            if (s % 10) % 2 != 0:
                p2 = p2 * (s % 10)
        s = s // 10
    R = abs(p1 - p2)
    if R == 29:
        print(M)
        break