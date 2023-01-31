for n in range(1,1000):
    x=bin(n)[2:]
    if x.count('1')%2==0:
        x=x[1:]
    else:
        x='1'+x+'00'
    if x.count('1') % 2 == 0:
        x = x[1:]
    else:
        x = '1' + x + '00'
    r=int(x,2)
    if r>100:
        print(n)
        brea