a=[int(x) for x in open('17_1.txt')]
b=sum(a)/len(a)
c=[]
for i in range(len(a)-1):
    if (a[i]>b or a[i+1]>b):
        c.append(a[i]+a[i+1])
print(len(c),max(c))