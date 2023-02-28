a=[int(x) for x in open('17-1.txt')]
a1=[]
for i in range(len(a)-1):
    s=sum(a)/len(a)
    if (a[i]>s or a[i+1]>s) and (a[i]%17==0 or a[i+1]%17==0):
        a1.append(a[i]+a[i+1])
print(len(a1),max(a1))