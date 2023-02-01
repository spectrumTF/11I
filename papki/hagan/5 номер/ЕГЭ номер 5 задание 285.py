for n in range(1,1000):
    x=bin(n)[2:]
    if n%2==0:
        x=x+"10"
    else:
        x="1"+x+"01"
    if int(x,2)>516:
        print(n)
        break