a=[int(x) for x in open('17_202.txt')]
b=[]
for i in range(len(a)-2):
    if (1000>a[i+1]>99 and a[i+1]%10==5):
        b.append(a[i]+a[i+1]+a[i+2])
print(len(b),max(b))
