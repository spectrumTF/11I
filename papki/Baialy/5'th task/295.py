for N in range(1, 500):
    k = bin(N) 
    s1 = k.count('1')**2
    for M in range(1, 500):
        k1 = bin(M) 
        s2 = k1.count('1')**2
        if (s1 - s2) == 33:
            print(N + M)
            break