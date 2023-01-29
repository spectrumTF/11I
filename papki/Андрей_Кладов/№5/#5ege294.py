for N in range(1000,10000):
    if N%2==0:
        x = str(N)
        x = sorted(x)
        x = ''.join(x)
        x = x[::-1]
        R = int(x)//2
    else:
        x = str(N)
        x = sorted(x)
        x = ''.join(x)
        R=int(x)*2
    if R==(N+1):
        print(R)
        break