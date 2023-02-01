
for x in range(1000,1,-1):
    f = bin(x)[2:]
    if f.count('1')%2 == 0:
        f ='10'+ f[2:]+'0'
    else:
        f ='11'+f[2:]+'1'
    r=int(f,2)
    if r<35:
        print(x)
        break