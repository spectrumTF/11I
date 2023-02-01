for i in range(1000,1,-1):
    n=i//2
    f=hex(n)[2:]
    if i%4!=0:
        f='f'+f+'a0'
    else:
        f='15'+f+'c'
    r=int(f,16)
    if r<65536:
        print(i)
        break