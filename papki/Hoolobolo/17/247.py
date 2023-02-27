a=[int(x)for x in open('17_243.txt')]
b=max([x for x in a if x%111==0])
c=[]
for i in range(len(a)-1):
    if ((a[i]>b or a[i+1]>b) and (abs(a[i])%10==7 or abs(a[i+1])%10==7)):
        c.append(a[i]+a[i+1])
print(len(c),min(c))