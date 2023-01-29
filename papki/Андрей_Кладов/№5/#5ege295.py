mi=2000
for N in range(1000):
    for M in range(1000):
        Sn=bin(N)[2:]
        Sn=(Sn.count('1'))**2
        Sm = bin(M)[2:]
        Sm = (Sm.count('1')) ** 2
        R=Sn-Sm
        if R==33 and (N+M)<mi:
            mi=N+M
print(mi)