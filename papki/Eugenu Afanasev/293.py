for m in range(10000):
    p=p1=1
    d=[int(c) for c in str(m)]
    for c in d:
        if c%2==0 and c>0:
            p*=c
        if c%2!=0:
            p1*=c
    p=p*2
    r=abs(p-p1)
    if r==29:
        print(m)
