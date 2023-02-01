def f(x):
    h=list(map(int,str(x)))
    a=sum(d for d in h if d%2==0)
    b=sum(h[1::2])
    return abs(a-b)
for x in range(100000000):
    if f(x)==29:
        print(x)
        break
