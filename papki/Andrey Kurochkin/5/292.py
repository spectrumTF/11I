for i in range(1,1000):
    n=bin(i)[2:]
    if i%2==0:
        n='10'+n[2:]+'0'
    else:
        n='11'+n[2:]+'1'
    r=int(n,2)
    if r<35:
        print(i)