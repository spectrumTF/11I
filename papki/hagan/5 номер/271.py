for i in range(1,1000):
    n=i
    a=''
    while n>0:
        a=str(n%4)+a
        n=n//4
    if i%2!=0:
        a='2'+a+'11'
    else:
        a='13'+a+'02'
        r=int(a,4)
        if r>1000:
            print(r)
            break