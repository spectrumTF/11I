a=[int(x)for x in open('17_4.txt')]
b=sum(a)/len(a)
c=[]
for i in range(len(a)-1):
    if (a[i]<b or a[i+1]<b) and ((a[i]%7==0 and a[i]%3!=0 and a[i]%11!=0 and a[i]%13!=0) or (a[i+1]%7==0 and a[i+1]%3!=0 and a[i+1]%11!=0 and a[i+1]%13!=0)):
        c.append(a[i]+a[i+1])
print(len(c),min(c))