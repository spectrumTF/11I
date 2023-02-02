for x in range(1,1000):
    a1=[]
    i=x
    while x!=0:
        a1.append(str(x%4))
        x//=4
    a1=a1[::-1]
    a1=int(''.join(a1))
    if i%2==0:
        a='13'+str(a1)+'02'
    else:
        a='2'+str(a1)+'11'
    r=int(a,4)
    if r>1000:
        print(r)
        break