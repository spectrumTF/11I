a=[int(x)for x in open('17_243.txt')]
b=max([x for x in a if x%119==0])
c=[]
for i in range(len(a)-1):
    if (a[i]<b and a[i+1]<b):
        c.append(a[i]+a[i+1])
print(len(c),max(c))