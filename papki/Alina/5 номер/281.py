for x in range(1,100000000):
    s1=0
    s2=0
    i=x
    while x!=0:
        if x%10%2==0:
            s1+=x%10
        x//=10    
    x=str(i)
    for i in range(len(x)-1,-1,-2):
        s2+=int(x[i])
    if abs(s1-s2)==26:
        print(x)
        break