a=[int(x)for x in open('17_4.txt')]
b=sum(a)/len(a)
c=[]
for i in range(len(a)-1):
    if (a[i]<b or a[i+1]<b) and ((not ('5' in str(a[i]))) or (not('5' in str(a[i+1])))):
        c.append(a[i]+a[i+1])
print(len(c),min(c))