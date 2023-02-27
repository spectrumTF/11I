a=[int(x)for x in open('17_1.txt')]
b=sum(a)/len(a)
c=[]
for i in range(len(a)-2):
    if (a[i]<b or a[i+1]<b or a[i+2]<b) and (((a[i])%7==0 and (a[i+1])%7==0) or ((a[i+1])%7==0 and a[i+2]%7==0) or (a[i]%7==0 and a[i+2]%7==0)) :
        c.append(a[i]+a[i+1]+a[i+2])
print(len(c),max(c))