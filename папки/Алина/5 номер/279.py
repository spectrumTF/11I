for x in range(1,10000000):
    s1=0
    s2=0
    i=x
    while x!=0:
        if x%10%2==1:
            s1+=x%10
        x//=10    
    x=str(i)
    for i in range(1,len(x),2):
        s2+=int(x[i])
    if 1<=int(x)<=9:
        s2=0    
    if abs(s1-s2)==29:
        print(x)
        break