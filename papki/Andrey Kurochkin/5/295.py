a=2000
for n in range(1000):
    for m in range(1000):
        S1=bin(n)[2:]
        S1=(S1.count('1'))**2
        S2 = bin(m)[2:]
        S2 = (S2.count('1')) ** 2
        r=S1-S2
        if r==33 and (n+m)<a:
            a=n+m
print(a)