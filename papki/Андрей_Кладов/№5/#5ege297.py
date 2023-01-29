for N in  range(10**16,10**17):
    x=str(N)[::-1]
    S=0
    for i in range(16):
        if i%2!=0:
            y1=int(x[i])*2
            if y1>9:
                S+=(1+(y1%10))
            else:
                S+=y1
        else:
            S+=int(x[i])
    if S==30:
        print(N)
        print('Ответ:',N%(10**8))
        break