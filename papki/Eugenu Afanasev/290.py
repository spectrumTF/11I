for x in range (100000000,1000000000):
    a=sum(map(int,str(x)))
    s=bin(a)[2:]
    if s.count('1')%2==0:
        s='1'+s+'00'
    else:
        s='10'+s+'1'
    r=int(s,2)
    if r==21:
        print(x)