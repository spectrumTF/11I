for x in range(1000,1,-1):
    i=x
    x1=x//2                     
    a1=hex(x1)[2:]
    if i%4==0:
        a='15'+str(a1)+'C'
    else:
        a='F'+str(a1)+'A0'    
    r=int(a,16)
    if r<65536:
        print(i)
        break