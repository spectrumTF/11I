a=[int(x)for x in open('17_1.txt')]
b=sum(a)/len(a)
c=[]
for i in range(len(a)-1):
    if (a[i]<b or a[i+1]<b) and (((abs(a[i]%3==0)) and (abs(a[i]%5!=0)) and (abs(a[i]%11!=0)) and (abs(a[i]%19!=0))) or (abs(a[i+1]%3==0)) and  (abs(a[i+1]%5!=0)) and (abs(a[i+1]%11!=0))and(abs(a[i+1]%19!=0))):
        c.append(a[i]+a[i+1])
print(len(c),max(c))