for n in range(1,10000):
    x=bin(n)[2:]
    if n %2!=0:
        x="10"+x+"11"
    else:
        x="1"+x+"00"
    r=int(x,2)
    if r>1023:
        print(r)
        break