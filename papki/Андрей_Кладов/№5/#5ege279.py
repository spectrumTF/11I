for n in range(1,10**8):
    x=str(n)
    S1=0
    S2=0
    for i in range(len(x)):
        if int(x[i])%2!=0:
            S1+=int(x[i])
        if (i+1)%2==0:
            S2 += int(x[i])
    if (S1-S2)<0:
        r=S2-S1
    else:
        r=S1-S2
    if r==29:
        print(n)
        break