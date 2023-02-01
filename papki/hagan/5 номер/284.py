c=0
for n in range(1,1000):
    x= bin(n)[2:]
    if n % 2==0:
        a=x.count("1")
        x=x+bin(a)[2:]
    else:
        x="1"+x+"00"
    r=int(x,2)
    if 500<=r<=700:
        c+=1
print(c)