for n in range(1,10000):
    f=''
    while n:
        f=str(n%4)+f
        n//=4
    if n%2!=0:
        f='2'+f+'11'
    else:
        f='13'+f+'02'
    r=int(f,4)
    if r>1000:
        print(r)
        break