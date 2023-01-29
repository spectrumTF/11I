for N in  range(1234567891011122,10**17):
    x=str(N)[::-1]
    y=0
    for i in range(16):
        if i%2!=0:
            y1=int(x[i])*2
            if y1>9:
                y+=(1+(y1%10))
            else:
                y+=y1
        else:
            y+=int(x[i])
    if y%10==0:
        print(N)
        print('Ответ:',str(N)[-8:])
        break