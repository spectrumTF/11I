for i in range(1,1000):
    n=bin(i)[2:]
    if i%2==0:
        n='10'+n+'1'
    else:
        n='1'+n+'01'
    if int(n,2)>420:
        print(i)
        break


# +