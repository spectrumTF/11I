a=[int(x) for x in open('17-202.txt')]
b=[]
for i in range(len(a)-2):
    if (1000>a[i+1]>99 and abs(a[i+1]%100==12)):
        b.append(a[i]+a[i+1]+a[i+2])
print(len(b),max(b))