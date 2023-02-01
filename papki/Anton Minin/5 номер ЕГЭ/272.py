for i in range(1000):
    n=bin(i)[2:]
    if i%4!=0:
        n='F'+n+'AO'
    else:
        n='15'+n+'C'
    r=int(n,16)
    if r<65536:
        print(i)
        break

# ???
