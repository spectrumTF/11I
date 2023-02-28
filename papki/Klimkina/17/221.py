a=[int(x) for x in open('17-1.txt')]
a1=[]
for i in range(len(a)-1):
    s=sum(a)/len(a)
    if (a[i]<s or a[i+1]<s) and ((a[i]%3==0 and a[i]%5!=0 and a[i]%11!=0 and a[i]%19!=0) or (a[i+1]%3==0 and a[i+1]%5!=0 and a[i+1]%11!=0 and a[i+1]%19!=0)):
        a1.append(a[i]+a[i+1])
print(len(a1),max(a1))