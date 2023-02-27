a=[int(x) for x in open('17_199.txt')]
b=[]
for i in range(len(a)-2):
    if (100>a[i+1]>9 and (a[i+1]%2==0)):
        b.append(a[i]+a[i+1]+a[i+2])
print(len(b),max(b))