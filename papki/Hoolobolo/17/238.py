a=[int(x)for x in open('17_1.txt')]
b=sum(a)/len(a)
c=[]
for i in range(len(a)-2):
    if (abs(a[i])%100==14 or abs(a[i+1])%100==14 or abs(a[i+2])%100==14) and ((a[i]<b and a[i+1]<b) or (a[i+1]<b and a[i+2]<b) or (a[i]<b and a[i+2]<b)) :
        c.append(a[i]+a[i+1]+a[i+2])
print(len(c),max(c))