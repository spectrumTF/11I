a=[int(x)for x in open('17_4.txt')]
b=sum(a)/len(a)
c=[]
for i in range(len(a)-1):
    if (a[i]<b and a[i+1]<b) and (abs(a[i])%100==19 or abs(a[i+1])%100==19):
        c.append(a[i]+a[i+1])
print(len(c),max(c))