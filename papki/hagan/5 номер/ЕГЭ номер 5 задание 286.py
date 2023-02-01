for n in range(1,1000):
    x= bin(n)[2:]
    if n%2==0:
        x="10"+x+"1"
    else:
        x="1"+x+"01"
    r=int(x,2)
    if r>420:
        print(n)
        break