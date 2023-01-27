for n in range(1,1000):
    x=bin(n)[2:]
    if x.count('1')%2==0:
        x= '10'+x[2:]+'0'
    else:
        x = '11' + x[2:] + '1'
    r=int(x,2)
    if r>=16:
        print(n)
        break