for i in range(1000,1,-1):
    f=bin(i)[2:]
    if i%2!=0:
        f='1'+f+'0'
    else:
        f='11'+f+'11'
    r=int(f,2)
    if r<126:
        print(i,r)
        