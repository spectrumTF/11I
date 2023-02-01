for x in range(100000):
    f=bin(x)[2:]
    if f.count('1')%2==0:
        f='10'+f[2:]+'0'
    else:
        f='11'+f[2:]+'1'
    r=int(f,2)
    if r>=16:
        print(x)
        break